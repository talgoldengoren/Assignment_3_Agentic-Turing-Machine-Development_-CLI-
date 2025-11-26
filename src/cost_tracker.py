"""
Cost Tracking Module

This module tracks API token usage and calculates costs for Claude API calls.
Provides detailed cost analysis and reporting for experiment runs.
"""

import json
from pathlib import Path
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from datetime import datetime

from config import get_config
from logger import get_logger

logger = get_logger(__name__)


@dataclass
class APICall:
    """
    Represents a single API call with token usage and cost information.

    Attributes:
        timestamp: When the call was made
        model: Model name used
        stage: Pipeline stage (1, 2, or 3)
        noise_level: Noise level being tested
        input_tokens: Number of input tokens
        output_tokens: Number of output tokens
        cost: Total cost in USD
    """
    timestamp: str
    model: str
    stage: int
    noise_level: int
    input_tokens: int
    output_tokens: int
    cost: float

    def to_dict(self) -> dict:
        """Convert to dictionary for JSON serialization."""
        return asdict(self)


class CostTracker:
    """
    Tracks and analyzes costs for API calls.

    Maintains a running total of token usage and costs,
    provides detailed breakdowns, and generates reports.

    Attributes:
        calls: List of API calls made
        config: Configuration instance
        enabled: Whether cost tracking is enabled
    """

    def __init__(self):
        """Initialize the cost tracker."""
        self.config = get_config()
        self.enabled = self.config.cost_tracking_enabled
        self.calls: List[APICall] = []

        logger.info(f"Cost tracking initialized (enabled={self.enabled})")

    def track_call(
        self,
        model: str,
        stage: int,
        noise_level: int,
        input_tokens: int,
        output_tokens: int
    ) -> float:
        """
        Track an API call and calculate its cost.

        Args:
            model: Model name (e.g., "claude-sonnet-4-20250514")
            stage: Pipeline stage number (1, 2, or 3)
            noise_level: Noise level percentage
            input_tokens: Number of input tokens used
            output_tokens: Number of output tokens generated

        Returns:
            Cost of the call in USD

        Example:
            >>> tracker = CostTracker()
            >>> cost = tracker.track_call("claude-sonnet-4", 1, 25, 150, 75)
            >>> print(f"Call cost: ${cost:.4f}")
        """
        if not self.enabled:
            return 0.0

        # Calculate cost
        cost = self._calculate_cost(model, input_tokens, output_tokens)

        # Record the call
        call = APICall(
            timestamp=datetime.now().isoformat(),
            model=model,
            stage=stage,
            noise_level=noise_level,
            input_tokens=input_tokens,
            output_tokens=output_tokens,
            cost=cost
        )
        self.calls.append(call)

        logger.debug(
            f"API call tracked: stage={stage}, noise={noise_level}, "
            f"tokens={input_tokens}+{output_tokens}, cost=${cost:.4f}"
        )

        return cost

    def _calculate_cost(
        self,
        model: str,
        input_tokens: int,
        output_tokens: int
    ) -> float:
        """
        Calculate cost for a single API call.

        Args:
            model: Model name
            input_tokens: Number of input tokens
            output_tokens: Number of output tokens

        Returns:
            Cost in USD
        """
        # Get pricing from config (per 1M tokens)
        model_key = self._get_model_key(model)
        pricing = self.config.get(f"cost_tracking.pricing.{model_key}", {})

        input_price_per_m = pricing.get("input", 3.00)  # Default to sonnet pricing
        output_price_per_m = pricing.get("output", 15.00)

        # Calculate cost (tokens / 1,000,000 * price_per_million)
        input_cost = (input_tokens / 1_000_000) * input_price_per_m
        output_cost = (output_tokens / 1_000_000) * output_price_per_m

        return input_cost + output_cost

    def _get_model_key(self, model: str) -> str:
        """
        Get the configuration key for a model.

        Args:
            model: Full model name

        Returns:
            Configuration key for the model
        """
        if "sonnet" in model.lower():
            return "claude-sonnet-4"
        elif "opus" in model.lower():
            return "claude-opus-4"
        elif "haiku" in model.lower():
            return "claude-haiku-4"
        return "claude-sonnet-4"  # Default

    def get_total_cost(self) -> float:
        """
        Get total cost of all tracked calls.

        Returns:
            Total cost in USD
        """
        return sum(call.cost for call in self.calls)

    def get_total_tokens(self) -> Dict[str, int]:
        """
        Get total token usage across all calls.

        Returns:
            Dictionary with 'input', 'output', and 'total' token counts
        """
        input_tokens = sum(call.input_tokens for call in self.calls)
        output_tokens = sum(call.output_tokens for call in self.calls)

        return {
            "input": input_tokens,
            "output": output_tokens,
            "total": input_tokens + output_tokens
        }

    def get_cost_by_stage(self) -> Dict[int, float]:
        """
        Get cost breakdown by pipeline stage.

        Returns:
            Dictionary mapping stage number to cost
        """
        costs = {1: 0.0, 2: 0.0, 3: 0.0}
        for call in self.calls:
            costs[call.stage] += call.cost
        return costs

    def get_cost_by_noise_level(self) -> Dict[int, float]:
        """
        Get cost breakdown by noise level.

        Returns:
            Dictionary mapping noise level to cost
        """
        costs: Dict[int, float] = {}
        for call in self.calls:
            if call.noise_level not in costs:
                costs[call.noise_level] = 0.0
            costs[call.noise_level] += call.cost
        return costs

    def get_summary(self) -> Dict:
        """
        Get comprehensive cost summary.

        Returns:
            Dictionary with complete cost analysis

        Example:
            >>> tracker = CostTracker()
            >>> # ... track some calls ...
            >>> summary = tracker.get_summary()
            >>> print(f"Total: ${summary['total_cost']:.2f}")
        """
        tokens = self.get_total_tokens()

        return {
            "total_cost": self.get_total_cost(),
            "total_calls": len(self.calls),
            "total_tokens": tokens,
            "cost_by_stage": self.get_cost_by_stage(),
            "cost_by_noise_level": self.get_cost_by_noise_level(),
            "average_cost_per_call": (
                self.get_total_cost() / len(self.calls)
                if self.calls else 0.0
            ),
            "currency": self.config.get("cost_tracking.cost_currency", "USD")
        }

    def save_report(self, output_file: Optional[Path] = None) -> Path:
        """
        Save cost report to JSON file.

        Args:
            output_file: Optional path for output file.
                        If None, uses config value

        Returns:
            Path where report was saved

        Raises:
            IOError: If file cannot be written
        """
        if output_file is None:
            report_filename = self.config.get(
                "cost_tracking.report.filename",
                "results/cost_analysis.json"
            )
            output_file = self.config.project_root / report_filename

        # Ensure directory exists
        output_file.parent.mkdir(parents=True, exist_ok=True)

        # Prepare report data
        report = {
            "generated_at": datetime.now().isoformat(),
            "summary": self.get_summary(),
            "calls": [call.to_dict() for call in self.calls]
            if self.config.get("cost_tracking.report.include_breakdown", True)
            else []
        }

        # Save to file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)

        logger.info(f"Cost report saved to {output_file}")
        return output_file

    def print_summary(self):
        """
        Print cost summary to console.

        Example:
            >>> tracker = CostTracker()
            >>> # ... track some calls ...
            >>> tracker.print_summary()
        """
        summary = self.get_summary()

        print("\n" + "=" * 70)
        print("COST ANALYSIS SUMMARY")
        print("=" * 70)
        print(f"Total Cost: ${summary['total_cost']:.4f} {summary['currency']}")
        print(f"Total API Calls: {summary['total_calls']}")
        print(f"Total Tokens: {summary['total_tokens']['total']:,}")
        print(f"  • Input: {summary['total_tokens']['input']:,}")
        print(f"  • Output: {summary['total_tokens']['output']:,}")
        print(f"Average Cost per Call: ${summary['average_cost_per_call']:.4f}")

        print("\nCost by Stage:")
        for stage, cost in sorted(summary['cost_by_stage'].items()):
            print(f"  Stage {stage}: ${cost:.4f}")

        print("\nCost by Noise Level:")
        for noise, cost in sorted(summary['cost_by_noise_level'].items()):
            print(f"  {noise}% noise: ${cost:.4f}")

        print("=" * 70 + "\n")


# Global cost tracker instance
_tracker: Optional[CostTracker] = None


def get_cost_tracker() -> CostTracker:
    """
    Get global cost tracker instance (singleton pattern).

    Returns:
        Global CostTracker instance
    """
    global _tracker
    if _tracker is None:
        _tracker = CostTracker()
    return _tracker


def reset_cost_tracker():
    """Reset the global cost tracker (useful for testing)."""
    global _tracker
    _tracker = CostTracker()
