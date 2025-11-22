#!/usr/bin/env python3
"""
Agentic Turing Machine - Results Analysis
==========================================

This script calculates semantic drift using vector embeddings and
visualizes the robustness of the LLM attention mechanism against noise.

Requirements:
- Python 3.7+
- openai library
- numpy
- matplotlib
- scikit-learn

Install with: pip install openai numpy matplotlib scikit-learn
"""

import os
import json
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics.pairwise import cosine_similarity
from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Original clean sentence
ORIGINAL_CLEAN = "The artificial intelligence system can efficiently process natural language and understand complex semantic relationships within textual data."

# Noise levels to analyze
NOISE_LEVELS = [0, 10, 20, 30, 40, 50]


def get_embedding(text: str, model: str = "text-embedding-3-small") -> list:
    """
    Get vector embedding for a given text using OpenAI's embedding API.
    
    Args:
        text: Input text to embed
        model: Embedding model to use
        
    Returns:
        List of floats representing the embedding vector
    """
    text = text.replace("\n", " ").strip()
    response = client.embeddings.create(input=[text], model=model)
    return response.data[0].embedding


def calculate_cosine_distance(vec1: list, vec2: list) -> float:
    """
    Calculate cosine distance between two vectors.
    Cosine distance = 1 - cosine similarity
    
    Args:
        vec1: First embedding vector
        vec2: Second embedding vector
        
    Returns:
        Float representing the cosine distance (0 = identical, 2 = opposite)
    """
    vec1 = np.array(vec1).reshape(1, -1)
    vec2 = np.array(vec2).reshape(1, -1)
    similarity = cosine_similarity(vec1, vec2)[0][0]
    distance = 1 - similarity
    return distance


def load_final_outputs() -> dict:
    """
    Load the final English outputs from each noise level experiment.
    
    Returns:
        Dictionary mapping noise level to final output text
    """
    outputs = {}
    
    for noise in NOISE_LEVELS:
        output_file = f"outputs/noise_{noise}/agent3_english.txt"
        
        if not os.path.exists(output_file):
            print(f"Warning: Output file not found for noise level {noise}%")
            print(f"Expected: {output_file}")
            continue
            
        with open(output_file, 'r', encoding='utf-8') as f:
            outputs[noise] = f.read().strip()
    
    return outputs


def analyze_semantic_drift():
    """
    Main analysis function:
    1. Load all final outputs
    2. Calculate embeddings for original and final outputs
    3. Compute cosine distances
    4. Generate visualization
    """
    print("=" * 60)
    print("SEMANTIC DRIFT ANALYSIS")
    print("=" * 60)
    print()
    
    # Load outputs
    print("Loading final outputs from agent chain...")
    final_outputs = load_final_outputs()
    
    if not final_outputs:
        print("Error: No output files found!")
        print("Please run the agent chain first: ./run_full_experiment.sh")
        return
    
    print(f"Loaded {len(final_outputs)} outputs")
    print()
    
    # Get embedding for original clean sentence
    print("Calculating embedding for original clean sentence...")
    original_embedding = get_embedding(ORIGINAL_CLEAN)
    print(f"Original embedding dimension: {len(original_embedding)}")
    print()
    
    # Calculate distances for each noise level
    print("Calculating semantic distances...")
    print("-" * 60)
    
    distances = {}
    
    for noise in sorted(final_outputs.keys()):
        final_text = final_outputs[noise]
        
        # Get embedding for final output
        final_embedding = get_embedding(final_text)
        
        # Calculate cosine distance
        distance = calculate_cosine_distance(original_embedding, final_embedding)
        distances[noise] = distance
        
        print(f"Noise {noise:2d}%: Distance = {distance:.6f}")
        print(f"  Original: {ORIGINAL_CLEAN[:60]}...")
        print(f"  Final:    {final_text[:60]}...")
        print()
    
    print("-" * 60)
    print()
    
    # Generate visualization
    print("Generating visualization...")
    generate_graph(distances)
    
    # Save results to JSON
    results = {
        "original_sentence": ORIGINAL_CLEAN,
        "final_outputs": final_outputs,
        "semantic_distances": distances,
        "embedding_model": "text-embedding-3-small",
        "distance_metric": "cosine_distance"
    }
    
    with open("analysis_results.json", 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    print("Results saved to: analysis_results.json")
    print("=" * 60)
    print()


def generate_graph(distances: dict):
    """
    Generate and save a graph showing semantic drift vs noise level.
    
    Args:
        distances: Dictionary mapping noise level to cosine distance
    """
    # Extract data
    noise_levels = sorted(distances.keys())
    distance_values = [distances[n] for n in noise_levels]
    
    # Create figure
    plt.figure(figsize=(12, 7))
    
    # Plot the data
    plt.plot(noise_levels, distance_values, 
             marker='o', 
             linewidth=2, 
             markersize=10,
             color='#2E86AB',
             markerfacecolor='#A23B72',
             markeredgewidth=2,
             markeredgecolor='#2E86AB')
    
    # Styling
    plt.xlabel('Spelling Error Rate (%)', fontsize=14, fontweight='bold')
    plt.ylabel('Vector Distance (Cosine Distance)', fontsize=14, fontweight='bold')
    plt.title('Semantic Drift in Multi-Agent Translation Pipeline\nEnglish → French → Hebrew → English',
              fontsize=16, fontweight='bold', pad=20)
    
    # Grid
    plt.grid(True, alpha=0.3, linestyle='--')
    
    # Add value labels on points
    for noise, distance in zip(noise_levels, distance_values):
        plt.annotate(f'{distance:.4f}',
                    xy=(noise, distance),
                    xytext=(0, 10),
                    textcoords='offset points',
                    ha='center',
                    fontsize=10,
                    bbox=dict(boxstyle='round,pad=0.3', 
                             facecolor='yellow', 
                             alpha=0.3))
    
    # Set axis ranges
    plt.xlim(-5, 55)
    plt.xticks(noise_levels)
    
    # Add interpretation text
    plt.text(0.02, 0.98, 
             'Lower distance = Better semantic preservation\nHigher distance = More semantic drift',
             transform=plt.gca().transAxes,
             fontsize=10,
             verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout()
    
    # Save figure
    plt.savefig('semantic_drift_analysis.png', dpi=300, bbox_inches='tight')
    print("Graph saved to: semantic_drift_analysis.png")
    
    # Also save as PDF for better quality
    plt.savefig('semantic_drift_analysis.pdf', bbox_inches='tight')
    print("Graph saved to: semantic_drift_analysis.pdf")
    
    plt.close()


def print_summary_statistics(distances: dict):
    """Print summary statistics of the experiment."""
    if not distances:
        return
    
    values = list(distances.values())
    print("SUMMARY STATISTICS")
    print("-" * 60)
    print(f"Mean distance:     {np.mean(values):.6f}")
    print(f"Median distance:   {np.median(values):.6f}")
    print(f"Std deviation:     {np.std(values):.6f}")
    print(f"Min distance:      {np.min(values):.6f} (at {min(distances, key=distances.get)}%)")
    print(f"Max distance:      {np.max(values):.6f} (at {max(distances, key=distances.get)}%)")
    print("-" * 60)


if __name__ == "__main__":
    # Check for API key
    if not os.environ.get("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY environment variable not set")
        print("Please set it with: export OPENAI_API_KEY='your-key-here'")
        exit(1)
    
    # Run analysis
    analyze_semantic_drift()


