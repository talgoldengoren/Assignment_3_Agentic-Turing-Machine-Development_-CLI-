# 🚀 Quick Start Guide

## Get Running in 5 Minutes

### Step 1: Install Dependencies

```bash
# Install jq (JSON processor)
# macOS:
brew install jq

# Linux (Ubuntu/Debian):
sudo apt-get install jq

# Install Python packages
pip install -r requirements.txt
```

### Step 2: Set API Key

```bash
export OPENAI_API_KEY='sk-your-actual-api-key-here'
```

💡 **Tip**: Add this to your `~/.zshrc` or `~/.bashrc` to make it permanent:
```bash
echo 'export OPENAI_API_KEY="sk-your-key-here"' >> ~/.zshrc
source ~/.zshrc
```

### Step 3: Make Scripts Executable

```bash
chmod +x run_agent_chain.sh run_full_experiment.sh
```

### Step 4: Run the Experiment

```bash
# Run the full experiment (all noise levels: 0%, 10%, 20%, 30%, 40%, 50%)
./run_full_experiment.sh
```

⏱️ **Expected time**: 2-3 minutes (depending on API response times)

### Step 5: Analyze Results

```bash
python3 analyze_results.py
```

🎉 **Done!** Check the outputs:
- `outputs/` - Intermediate and final translations
- `semantic_drift_analysis.png` - Visualization
- `analysis_results.json` - Detailed results

---

## Testing Single Noise Level

Want to test just one noise level?

```bash
./run_agent_chain.sh 30 "The artifical inteligence systm can eficiently proces natural langauge and understnd complex semantic relationships within textual data."
```

---

## Verifying Installation

### Check if jq is installed:
```bash
jq --version
# Should output: jq-1.6 or similar
```

### Check if Python packages are installed:
```bash
python3 -c "import openai, numpy, matplotlib, sklearn; print('All packages installed!')"
```

### Check if API key is set:
```bash
echo $OPENAI_API_KEY
# Should output your API key (starts with sk-)
```

---

## Troubleshooting

### Issue: "Permission denied"
**Solution**:
```bash
chmod +x run_agent_chain.sh run_full_experiment.sh
```

### Issue: "jq: command not found"
**Solution**: Install jq (see Step 1)

### Issue: "OPENAI_API_KEY environment variable not set"
**Solution**: Set your API key (see Step 2)

### Issue: API rate limit errors
**Solution**: Increase the sleep time in `run_full_experiment.sh`:
```bash
# Change this line:
sleep 2
# To:
sleep 5
```

---

## What's Happening?

1. **Agent Chain Execution** (`run_full_experiment.sh`):
   - Takes English sentences with different noise levels
   - Agent 1: Translates to French (ignoring spelling errors)
   - Agent 2: Translates to Hebrew
   - Agent 3: Translates back to English
   - Saves all outputs

2. **Analysis** (`analyze_results.py`):
   - Compares final English output with original clean sentence
   - Uses vector embeddings to measure semantic similarity
   - Calculates cosine distance (semantic drift)
   - Creates visualization graph

---

## Expected Results

Your graph should show:
- **X-axis**: Spelling error percentage (0% to 50%)
- **Y-axis**: Semantic distance (drift from original)
- **Trend**: Ideally flat or slowly increasing (showing LLM robustness)

Lower distance = Better semantic preservation 🎯

---

## Next Steps

1. Review the outputs in `outputs/` directory
2. Examine the graph: `semantic_drift_analysis.png`
3. Check detailed results: `analysis_results.json`
4. Read the full documentation: `README.md`

---

Happy experimenting! 🧪✨


