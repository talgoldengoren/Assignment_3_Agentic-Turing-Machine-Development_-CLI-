#!/bin/bash

# Setup Verification Script
# Run this to check if everything is properly configured

echo "========================================"
echo "Agentic Turing Machine - Setup Verification"
echo "========================================"
echo ""

ERRORS=0

# Check 1: jq installation
echo -n "Checking for jq... "
if command -v jq &> /dev/null; then
    VERSION=$(jq --version)
    echo "✓ Found ($VERSION)"
else
    echo "✗ NOT FOUND"
    echo "  Install with: brew install jq (macOS) or apt-get install jq (Linux)"
    ERRORS=$((ERRORS + 1))
fi

# Check 2: curl installation
echo -n "Checking for curl... "
if command -v curl &> /dev/null; then
    VERSION=$(curl --version | head -n 1)
    echo "✓ Found"
else
    echo "✗ NOT FOUND"
    ERRORS=$((ERRORS + 1))
fi

# Check 3: Python installation
echo -n "Checking for Python 3... "
if command -v python3 &> /dev/null; then
    VERSION=$(python3 --version)
    echo "✓ Found ($VERSION)"
else
    echo "✗ NOT FOUND"
    ERRORS=$((ERRORS + 1))
fi

# Check 4: OPENAI_API_KEY
echo -n "Checking for OPENAI_API_KEY... "
if [ -z "$OPENAI_API_KEY" ]; then
    echo "✗ NOT SET"
    echo "  Set with: export OPENAI_API_KEY='your-key-here'"
    ERRORS=$((ERRORS + 1))
else
    KEY_PREFIX=$(echo "$OPENAI_API_KEY" | cut -c1-7)
    KEY_LENGTH=${#OPENAI_API_KEY}
    echo "✓ Set (${KEY_PREFIX}..., length: $KEY_LENGTH)"
fi

# Check 5: Python packages
echo -n "Checking Python packages... "
if python3 -c "import openai, numpy, matplotlib, sklearn" 2>/dev/null; then
    echo "✓ All required packages installed"
else
    echo "✗ Missing packages"
    echo "  Install with: pip install -r requirements.txt"
    ERRORS=$((ERRORS + 1))
fi

# Check 6: Required files
echo ""
echo "Checking required files:"

FILES=(
    "agent1_skill.txt"
    "agent2_skill.txt"
    "agent3_skill.txt"
    "input_data.txt"
    "run_agent_chain.sh"
    "run_full_experiment.sh"
    "analyze_results.py"
    "requirements.txt"
)

for file in "${FILES[@]}"; do
    echo -n "  $file... "
    if [ -f "$file" ]; then
        echo "✓"
    else
        echo "✗ MISSING"
        ERRORS=$((ERRORS + 1))
    fi
done

# Check 7: Script permissions
echo ""
echo "Checking script permissions:"

SCRIPTS=(
    "run_agent_chain.sh"
    "run_full_experiment.sh"
)

for script in "${SCRIPTS[@]}"; do
    echo -n "  $script... "
    if [ -x "$script" ]; then
        echo "✓ Executable"
    else
        echo "⚠ Not executable (will fix automatically)"
        chmod +x "$script"
    fi
done

# Summary
echo ""
echo "========================================"
if [ $ERRORS -eq 0 ]; then
    echo "✓ ALL CHECKS PASSED!"
    echo "========================================"
    echo ""
    echo "You're ready to run the experiment:"
    echo "  ./run_full_experiment.sh"
    echo ""
else
    echo "✗ FOUND $ERRORS ERROR(S)"
    echo "========================================"
    echo ""
    echo "Please fix the errors above before running the experiment."
    echo ""
fi


