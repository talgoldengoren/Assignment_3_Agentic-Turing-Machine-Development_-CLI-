#!/usr/bin/env python3
"""
Agentic Turing Machine - Run with Claude Agent Skills
======================================================

This script runs the translation chain experiment using Claude's Agent Skills feature.
It demonstrates how to invoke specialized agent skills through the Anthropic API.

Usage:
    python3 run_with_skills.py --noise 25
    python3 run_with_skills.py --all  # Run all noise levels

Requirements:
    pip install anthropic
    export ANTHROPIC_API_KEY='your-key-here'
"""

import os
import sys
import argparse
from pathlib import Path
from typing import Optional, Tuple
import anthropic

# Import configuration management
from config import get_config

# Import error handling, logging, and cost tracking
from errors import (
    SkillNotFoundError,
    InvalidNoiseLevel,
    TranslationError,
    APIError,
    ConfigurationError
)
from logger import get_logger
from cost_tracker import get_cost_tracker

# Get configuration instance
config = get_config()

# Set up logging
logger = get_logger(__name__)

# Get cost tracker
cost_tracker = get_cost_tracker()

# Load constants from configuration (backward compatibility)
SKILLS_DIR = config.skills_dir
ORIGINAL_CLEAN = config.original_sentence
NOISY_INPUTS = config.noisy_inputs


def load_skill(skill_name: str) -> dict:
    """
    Load a skill's SKILL.md content from the skills directory.

    This function loads the skill definition file which contains the instructions
    and behavior for a specific translation agent (e.g., English→French translator).

    Args:
        skill_name: Name of the skill directory (e.g., "english-to-french-translator")

    Returns:
        Dictionary containing:
            - name (str): The skill name
            - content (str): The skill file content

    Raises:
        SkillNotFoundError: If the skill file doesn't exist
        IOError: If the skill file cannot be read

    Example:
        >>> skill = load_skill("english-to-french-translator")
        >>> print(skill["name"])
        english-to-french-translator
    """
    skill_path = SKILLS_DIR / skill_name / "SKILL.md"

    if not skill_path.exists():
        logger.error(f"Skill not found: {skill_path}")
        raise SkillNotFoundError(
            f"Skill not found: {skill_name}",
            details={"path": str(skill_path)}
        )

    try:
        with open(skill_path, 'r', encoding='utf-8') as f:
            content = f.read()

        logger.debug(f"Loaded skill: {skill_name} ({len(content)} characters)")

        return {
            "name": skill_name,
            "content": content
        }
    except IOError as e:
        logger.error(f"Failed to read skill file: {skill_path}", exc_info=True)
        raise SkillNotFoundError(
            f"Cannot read skill file: {skill_name}",
            details={"path": str(skill_path), "error": str(e)}
        )


def run_translation_with_skill(
    client: anthropic.Anthropic,
    skill_name: str,
    input_text: str,
    stage: int,
    noise_level: int = 0
) -> Tuple[str, Optional[int], Optional[int]]:
    """
    Run a single translation using a specific Claude Agent skill.

    This function loads a skill definition, constructs a prompt with the skill
    instructions and input text, calls the Claude API, and returns the translated
    output along with token usage information for cost tracking.

    Args:
        client: Initialized Anthropic API client with valid API key
        skill_name: Name of the skill to use (must exist in skills directory)
        input_text: Text to translate (can contain spelling errors)
        stage: Pipeline stage number (1=English→French, 2=French→Hebrew, 3=Hebrew→English)
        noise_level: Noise level percentage for cost tracking (default: 0)

    Returns:
        Tuple containing:
            - Translated text (str)
            - Input tokens used (int or None if tracking disabled)
            - Output tokens generated (int or None if tracking disabled)

    Raises:
        SkillNotFoundError: If the specified skill doesn't exist
        APIError: If the Claude API call fails
        TranslationError: If translation produces invalid output

    Example:
        >>> client = anthropic.Anthropic(api_key="...")
        >>> text, input_tok, output_tok = run_translation_with_skill(
        ...     client, "english-to-french-translator", "Hello world", 1
        ... )
        >>> print(f"Translation: {text}")
        >>> print(f"Cost: {input_tok} + {output_tok} tokens")
    """
    logger.info(f"Stage {stage}: Starting translation with {skill_name}")

    # Load the skill definition
    try:
        skill = load_skill(skill_name)
    except SkillNotFoundError as e:
        logger.error(f"Failed to load skill: {e}")
        raise

    # Construct the prompt with skill instructions and input
    prompt = f"""You are using the "{skill_name}" skill.

{skill['content']}

---

Please translate the following text according to the skill instructions above.
Return ONLY the translation, with no explanations or additional text.

Input text:
{input_text}"""

    print(f"  Stage {stage}: Invoking {skill_name}...")
    logger.debug(f"Calling API with {len(input_text)} character input")

    try:
        # Call Claude API
        response = client.messages.create(
            model=config.model_name,
            max_tokens=config.max_tokens,
            temperature=config.temperature,  # Deterministic for consistency
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )

        # Extract the text content
        output = response.content[0].text.strip()

        # Extract token usage
        input_tokens = response.usage.input_tokens
        output_tokens = response.usage.output_tokens

        # Track cost if enabled
        if cost_tracker.enabled:
            cost = cost_tracker.track_call(
                model=config.model_name,
                stage=stage,
                noise_level=noise_level,
                input_tokens=input_tokens,
                output_tokens=output_tokens
            )
            logger.debug(
                f"API call completed: {input_tokens}+{output_tokens} tokens, "
                f"cost=${cost:.4f}"
            )

        print(f"  ✓ Stage {stage} complete: {len(output)} characters")
        logger.info(f"Stage {stage}: Translation successful ({len(output)} chars)")

        return output, input_tokens, output_tokens

    except anthropic.APIError as e:
        logger.error(f"API error in stage {stage}: {e}", exc_info=True)
        print(f"  ✗ Error in stage {stage}: {e}")
        raise APIError(
            f"Claude API call failed at stage {stage}",
            details={"stage": stage, "skill": skill_name, "error": str(e)}
        )
    except Exception as e:
        logger.error(f"Unexpected error in stage {stage}: {e}", exc_info=True)
        print(f"  ✗ Error in stage {stage}: {e}")
        raise TranslationError(
            f"Translation failed at stage {stage}",
            details={"stage": stage, "skill": skill_name, "error": str(e)}
        )


def run_translation_chain(noise_level: int):
    """
    Run the complete three-stage translation chain for a given noise level.

    This function orchestrates the entire translation pipeline:
    1. English → French (handles noisy input)
    2. French → Hebrew (bridges language families)
    3. Hebrew → English (completes round-trip)

    Each stage's output is saved to disk and used as input for the next stage.
    Token usage and costs are tracked automatically if cost tracking is enabled.

    Args:
        noise_level: Percentage of spelling errors in input (0, 10, 20, 25, 30, 40, or 50)

    Raises:
        ConfigurationError: If API key is not configured
        InvalidNoiseLevel: If noise_level is not in the valid set
        TranslationError: If any translation stage fails
        IOError: If output files cannot be written

    Example:
        >>> run_translation_chain(25)  # Run with 25% noise
        ======================================================================
        RUNNING TRANSLATION CHAIN - Noise Level: 25%
        ======================================================================
        ...
        ✓ Translation chain complete!
    """
    logger.info(f"Starting translation chain for noise level {noise_level}%")

    # Validate API key using configuration
    api_key = config.api_key
    if not api_key:
        error_msg = "ANTHROPIC_API_KEY environment variable not set"
        logger.error(error_msg)
        print(f"Error: {error_msg}")
        print("Please set it with: export ANTHROPIC_API_KEY='your-key-here'")
        raise ConfigurationError(error_msg)

    # Initialize Anthropic client
    client = anthropic.Anthropic(api_key=api_key)

    # Validate noise level
    if noise_level not in NOISY_INPUTS:
        error_msg = f"Invalid noise level {noise_level}"
        logger.error(f"{error_msg}. Valid levels: {list(NOISY_INPUTS.keys())}")
        print(f"Error: {error_msg}. Must be one of: {list(NOISY_INPUTS.keys())}")
        raise InvalidNoiseLevel(
            error_msg,
            details={"noise_level": noise_level, "valid_levels": list(NOISY_INPUTS.keys())}
        )

    input_text = NOISY_INPUTS[noise_level]

    print("=" * 70)
    print(f"RUNNING TRANSLATION CHAIN - Noise Level: {noise_level}%")
    print("=" * 70)
    print(f"Input: {input_text[:60]}...")
    print()

    # Create output directory using configuration
    output_dir = config.output_dir / f"noise_{noise_level}"
    try:
        output_dir.mkdir(parents=True, exist_ok=True)
        logger.debug(f"Output directory created: {output_dir}")
    except OSError as e:
        logger.error(f"Failed to create output directory: {e}", exc_info=True)
        raise

    # Stage 1: English → French
    french_output, _, _ = run_translation_with_skill(
        client,
        "english-to-french-translator",
        input_text,
        stage=1,
        noise_level=noise_level
    )
    
    # Save French output
    with open(output_dir / "agent1_french.txt", 'w', encoding='utf-8') as f:
        f.write(french_output + "\n")
    
    print(f"  Saved: {output_dir}/agent1_french.txt")
    print()
    
    # Stage 2: French → Hebrew
    hebrew_output, _, _ = run_translation_with_skill(
        client,
        "french-to-hebrew-translator",
        french_output,
        stage=2,
        noise_level=noise_level
    )

    # Save Hebrew output
    with open(output_dir / "agent2_hebrew.txt", 'w', encoding='utf-8') as f:
        f.write(hebrew_output + "\n")

    print(f"  Saved: {output_dir}/agent2_hebrew.txt")
    print()

    # Stage 3: Hebrew → English
    english_output, _, _ = run_translation_with_skill(
        client,
        "hebrew-to-english-translator",
        hebrew_output,
        stage=3,
        noise_level=noise_level
    )

    # Save English output
    with open(output_dir / "agent3_english.txt", 'w', encoding='utf-8') as f:
        f.write(english_output + "\n")

    print(f"  Saved: {output_dir}/agent3_english.txt")
    print()
    
    # Summary
    print("-" * 70)
    print("TRANSLATION CHAIN COMPLETE")
    print("-" * 70)
    print(f"Original: {ORIGINAL_CLEAN}")
    print(f"Final:    {english_output}")
    print()
    print(f"All outputs saved to: {output_dir}")

    # Print cost summary if tracking is enabled
    if cost_tracker.enabled:
        summary = cost_tracker.get_summary()
        print()
        print(f"💰 Cost for this run: ${summary['total_cost']:.4f} USD")
        print(f"📊 Tokens used: {summary['total_tokens']['total']:,} "
              f"({summary['total_tokens']['input']:,} input + "
              f"{summary['total_tokens']['output']:,} output)")

    print("=" * 70)
    print()

    logger.info(f"Translation chain completed successfully for noise level {noise_level}%")


def main():
    """
    Main entry point for the translation chain experiment.

    Parses command-line arguments and runs the translation pipeline for
    either a single noise level or all noise levels. Generates cost reports
    if cost tracking is enabled.

    Command-line arguments:
        --noise LEVEL: Run experiment with specific noise level (0-50%)
        --all: Run experiment with all noise levels (0, 10, 20, 25, 30, 40, 50%)

    Examples:
        $ python3 run_with_skills.py --noise 25
        $ python3 run_with_skills.py --all

    Exit codes:
        0: Success
        1: Error (missing arguments, invalid configuration, etc.)
    """
    logger.info("Starting Agentic Turing Machine pipeline")

    parser = argparse.ArgumentParser(
        description="Run translation chain experiment using Claude Agent Skills",
        epilog="Example: python3 run_with_skills.py --all"
    )
    parser.add_argument(
        "--noise",
        type=int,
        choices=[0, 10, 20, 25, 30, 40, 50],
        help="Noise level percentage (0, 10, 20, 25, 30, 40, or 50)"
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Run all noise levels (0%%, 10%%, 20%%, 25%%, 30%%, 40%%, 50%%)"
    )

    args = parser.parse_args()

    # Validate arguments
    if not args.noise and not args.all:
        parser.print_help()
        print("\nError: Specify --noise LEVEL or --all")
        logger.error("No noise level specified")
        sys.exit(1)

    # Validate skills directory exists
    if not SKILLS_DIR.exists():
        error_msg = f"Skills directory not found: {SKILLS_DIR}"
        logger.error(error_msg)
        print(f"Error: {error_msg}")
        print("Please ensure the skills/ directory exists with SKILL.md files")
        sys.exit(1)

    # Run experiment(s)
    try:
        if args.all:
            print("Running full experiment with all noise levels...")
            print()
            logger.info("Running experiments for all noise levels")

            for noise_level in config.noise_levels:
                try:
                    run_translation_chain(noise_level)
                except Exception as e:
                    logger.error(
                        f"Error at noise level {noise_level}: {e}",
                        exc_info=True
                    )
                    print(f"⚠ Error at noise level {noise_level}: {e}")
                    print("Continuing with next level...")
                    continue
        else:
            logger.info(f"Running experiment for noise level {args.noise}%")
            run_translation_chain(args.noise)

    except KeyboardInterrupt:
        logger.warning("Experiment interrupted by user")
        print("\n\n⚠ Experiment interrupted by user")
        sys.exit(130)

    # Generate and save cost report if enabled
    if cost_tracker.enabled and len(cost_tracker.calls) > 0:
        print()
        cost_tracker.print_summary()

        try:
            report_path = cost_tracker.save_report()
            print(f"💾 Cost report saved to: {report_path}")
            logger.info(f"Cost report saved to {report_path}")
        except Exception as e:
            logger.error(f"Failed to save cost report: {e}", exc_info=True)
            print(f"⚠ Warning: Could not save cost report: {e}")

    print()
    print("✓ Experiment complete!")
    print(f"📊 Next step: python3 analyze_results_local.py")
    logger.info("Pipeline execution completed successfully")


if __name__ == "__main__":
    main()

