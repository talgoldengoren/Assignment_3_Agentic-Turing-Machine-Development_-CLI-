#!/bin/bash

# Master Script: Run Full Experiment Across All Noise Levels
# This executes the agent chain for 0%, 10%, 20%, 30%, 40%, 50% noise

set -e

echo "========================================"
echo "AGENTIC TURING MACHINE - FULL EXPERIMENT"
echo "========================================"
echo ""

# Check prerequisites
if [ -z "$OPENAI_API_KEY" ]; then
    echo "Error: OPENAI_API_KEY environment variable not set"
    echo "Please set it with: export OPENAI_API_KEY='your-key-here'"
    exit 1
fi

if ! command -v jq &> /dev/null; then
    echo "Error: jq is required but not installed"
    echo "Install it with: brew install jq (macOS) or apt-get install jq (Linux)"
    exit 1
fi

# Make the agent chain script executable
chmod +x run_agent_chain.sh

# Clean sentence
CLEAN="The artificial intelligence system can efficiently process natural language and understand complex semantic relationships within textual data."

# Define noise levels and corresponding inputs
declare -A INPUTS
INPUTS[0]="The artificial intelligence system can efficiently process natural language and understand complex semantic relationships within textual data."
INPUTS[10]="The artifical intelligence systm can efficiently process natural language and understand complex semantic relationships within textual data."
INPUTS[20]="The artifical inteligence systm can efficiently proces natural language and understand complex semantic relationships within textual data."
INPUTS[30]="The artifical inteligence systm can eficiently proces natural langauge and understnd complex semantic relationships within textual data."
INPUTS[40]="The artifical inteligence systm can eficiently proces naturel langauge and understnd complx semantic relatioships within textual data."
INPUTS[50]="The artifical inteligence systm can eficiently proces naturel langauge and understnd complx semantic relatioships withn textul data."

# Run for each noise level
for noise in 0 10 20 30 40 50; do
    echo ""
    echo "========================================" echo "Testing with ${noise}% spelling errors"
    echo "========================================"
    
    input="${INPUTS[$noise]}"
    
    ./run_agent_chain.sh "$noise" "$input"
    
    echo ""
    echo "Completed noise level: ${noise}%"
    echo "Waiting 2 seconds before next run..."
    sleep 2
done

echo ""
echo "========================================"
echo "EXPERIMENT COMPLETE!"
echo "========================================"
echo "All results saved to outputs/ directory"
echo ""
echo "Next step: Run the Python analysis script"
echo "Command: python3 analyze_results.py"
echo "========================================"


