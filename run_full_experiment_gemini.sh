#!/bin/bash

# Agentic Turing Machine - Full Experiment Runner (Google Gemini Version)
# Runs the agent chain for all noise levels: 0%, 10%, 20%, 30%, 40%, 50%
# Uses Google Gemini API

set -e  # Exit on error

# Check if GOOGLE_API_KEY is set
if [ -z "$GOOGLE_API_KEY" ]; then
    echo "Error: GOOGLE_API_KEY environment variable not set"
    echo "Please set it with: export GOOGLE_API_KEY='your-key-here'"
    exit 1
fi

echo "========================================"
echo "AGENTIC TURING MACHINE - FULL EXPERIMENT"
echo "Using Google Gemini API (gemini-2.0-flash)"
echo "========================================"
echo ""
echo "This will run the agent chain for noise levels: 0%, 10%, 20%, 30%, 40%, 50%"
echo "Estimated time: 2-3 minutes"
echo "Total API calls: 18 (3 per noise level)"
echo ""

# Input sentences from input_data.txt
NOISE_0="The artificial intelligence system can efficiently process natural language and understand complex semantic relationships within textual data."
NOISE_10="The artifical intelligence systm can efficiently process natural language and understand complex semantic relationships within textual data."
NOISE_20="The artifical inteligence systm can efficiently proces natural language and understand complex semantic relationships within textual data."
NOISE_30="The artifical inteligence systm can eficiently proces natural langauge and understnd complex semantic relationships within textual data."
NOISE_40="The artifical inteligence systm can eficiently proces naturel langauge and understnd complx semantic relatioships within textual data."
NOISE_50="The artifical inteligence systm can eficiently proces naturel langauge and understnd complx semantic relatioships withn textul data."

# Run experiments
echo "========================================"
echo "Running Experiment 1/6: Noise Level 0%"
echo "========================================"
./run_agent_chain_gemini.sh 0 "$NOISE_0"
echo ""
sleep 2

echo "========================================"
echo "Running Experiment 2/6: Noise Level 10%"
echo "========================================"
./run_agent_chain_gemini.sh 10 "$NOISE_10"
echo ""
sleep 2

echo "========================================"
echo "Running Experiment 3/6: Noise Level 20%"
echo "========================================"
./run_agent_chain_gemini.sh 20 "$NOISE_20"
echo ""
sleep 2

echo "========================================"
echo "Running Experiment 4/6: Noise Level 30%"
echo "========================================"
./run_agent_chain_gemini.sh 30 "$NOISE_30"
echo ""
sleep 2

echo "========================================"
echo "Running Experiment 5/6: Noise Level 40%"
echo "========================================"
./run_agent_chain_gemini.sh 40 "$NOISE_40"
echo ""
sleep 2

echo "========================================"
echo "Running Experiment 6/6: Noise Level 50%"
echo "========================================"
./run_agent_chain_gemini.sh 50 "$NOISE_50"
echo ""

echo "========================================"
echo "EXPERIMENT COMPLETE!"
echo "========================================"
echo ""
echo "Results saved in: outputs/"
echo ""
echo "Next steps:"
echo "1. Run analysis: python analyze_results_gemini.py"
echo "2. View graph: open semantic_drift_analysis.png"
echo ""

