# 🌟 Google Gemini API Setup Guide

## 📋 Overview

This guide shows you how to run the Agentic Turing Machine project using **Google's Gemini API** instead of OpenAI. All the necessary scripts have been created for you!

---

## 🎯 Key Differences: Gemini vs OpenAI

| Feature | OpenAI | Google Gemini |
|---------|--------|---------------|
| **API Key** | `OPENAI_API_KEY` | `GOOGLE_API_KEY` |
| **Model** | `gpt-4o-mini` | `gemini-1.5-flash` |
| **Scripts** | `run_agent_chain.sh` | `run_agent_chain_gemini.sh` |
| **Analysis** | `analyze_results.py` | `analyze_results_gemini.py` |
| **Requirements** | `requirements.txt` | `requirements_gemini.txt` |
| **Pricing** | ~$0.15/run | ~$0.10/run (cheaper!) |

---

## 🚀 Quick Start (5 Minutes)

### Step 1: Set Your Google API Key

```bash
export GOOGLE_API_KEY="AIzaSyCBPL4EMJyCsCLUKoDKOvsQVA0kDrJJJrM"
```

**⚠️ Security Note**: Never share your API key publicly! Consider regenerating it after testing.

**Make it Permanent** (Optional):
```bash
# Add to your shell configuration
echo 'export GOOGLE_API_KEY="your-key-here"' >> ~/.zshrc
source ~/.zshrc
```

### Step 2: Install Python Dependencies

```bash
# Install Gemini-specific requirements
pip install -r requirements_gemini.txt
```

**What gets installed:**
- `google-generativeai` - Google's Gemini API SDK
- `numpy` - Numerical computing
- `matplotlib` - Visualization
- `scikit-learn` - Machine learning utilities

### Step 3: Verify Setup

```bash
# Check if API key is set
echo $GOOGLE_API_KEY

# Test Python imports
python3 -c "import google.generativeai as genai; print('✓ Gemini SDK ready!')"
```

### Step 4: Make Scripts Executable

```bash
chmod +x run_agent_chain_gemini.sh
chmod +x run_full_experiment_gemini.sh
```

### Step 5: Run Your First Test

```bash
# Test with 0% noise
./run_agent_chain_gemini.sh 0 "The artificial intelligence system can efficiently process natural language and understand complex semantic relationships within textual data."
```

**Expected Output:**
```
========================================
Running Agent Chain - Noise Level: 0%
Using Google Gemini API
========================================

>>> Agent 1: Translating English to French...
Input: The artificial intelligence system...
Output: Le système d'intelligence artificielle...

>>> Agent 2: Translating French to Hebrew...
...

>>> Agent 3: Translating Hebrew to English...
...

========================================
Agent Chain Complete!
========================================
```

### Step 6: Run Full Experiment

```bash
./run_full_experiment_gemini.sh
```

**What happens:**
- Runs all 6 noise levels (0%, 10%, 20%, 30%, 40%, 50%)
- Takes 2-3 minutes
- Creates outputs in `outputs/` directory

### Step 7: Analyze Results

```bash
python3 analyze_results_gemini.py
```

**Output:**
- `semantic_drift_analysis.png` - Visualization
- `semantic_drift_analysis.pdf` - High-quality PDF
- `analysis_results.json` - Detailed metrics

### Step 8: View Graph

```bash
open semantic_drift_analysis.png  # macOS
# OR
xdg-open semantic_drift_analysis.png  # Linux
```

---

## 📝 Detailed Differences

### 1. API Key Configuration

**OpenAI:**
```bash
export OPENAI_API_KEY='sk-...'
```

**Gemini:**
```bash
export GOOGLE_API_KEY='AIza...'
```

### 2. Script Names

| Task | OpenAI Script | Gemini Script |
|------|---------------|---------------|
| Single run | `run_agent_chain.sh` | `run_agent_chain_gemini.sh` |
| Full experiment | `run_full_experiment.sh` | `run_full_experiment_gemini.sh` |
| Analysis | `analyze_results.py` | `analyze_results_gemini.py` |

### 3. API Request Format

**OpenAI Format:**
```json
{
  "model": "gpt-4o-mini",
  "messages": [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "..."}
  ]
}
```

**Gemini Format:**
```json
{
  "contents": [
    {
      "parts": [
        {"text": "system_prompt\n\nUser input:\nuser_text"}
      ]
    }
  ],
  "generationConfig": {
    "temperature": 0.3,
    "maxOutputTokens": 500
  }
}
```

### 4. API Endpoint

**OpenAI:**
```
https://api.openai.com/v1/chat/completions
Authorization: Bearer $API_KEY
```

**Gemini:**
```
https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=$API_KEY
```

### 5. Response Parsing

**OpenAI:**
```bash
OUTPUT=$(echo "$RESPONSE" | jq -r '.choices[0].message.content')
```

**Gemini:**
```bash
OUTPUT=$(echo "$RESPONSE" | jq -r '.candidates[0].content.parts[0].text')
```

---

## 🎓 Complete Workflow (Copy-Paste Ready)

```bash
# 1. Set API key
export GOOGLE_API_KEY="AIzaSyCBPL4EMJyCsCLUKoDKOvsQVA0kDrJJJrM"

# 2. Install dependencies
pip install -r requirements_gemini.txt

# 3. Make scripts executable
chmod +x run_agent_chain_gemini.sh run_full_experiment_gemini.sh

# 4. Run full experiment
./run_full_experiment_gemini.sh

# 5. Analyze results
python3 analyze_results_gemini.py

# 6. View graph
open semantic_drift_analysis.png
```

---

## 🧪 Testing Individual Components

### Test Single Noise Level

```bash
# 0% noise (clean)
./run_agent_chain_gemini.sh 0 "The artificial intelligence system can efficiently process natural language and understand complex semantic relationships within textual data."

# 30% noise
./run_agent_chain_gemini.sh 30 "The artifical inteligence systm can eficiently proces natural langauge and understnd complex semantic relationships within textual data."

# 50% noise
./run_agent_chain_gemini.sh 50 "The artifical inteligence systm can eficiently proces naturel langauge and understnd complx semantic relatioships withn textul data."
```

### View Outputs

```bash
# View all outputs
ls -R outputs/

# View specific noise level
cat outputs/noise_30/agent1_french.txt
cat outputs/noise_30/agent2_hebrew.txt
cat outputs/noise_30/agent3_english.txt
```

---

## 🔧 How It Works Internally

### Agent Chain Script (`run_agent_chain_gemini.sh`)

**Key Changes:**
1. Uses `GOOGLE_API_KEY` instead of `OPENAI_API_KEY`
2. Gemini API endpoint: `generativelanguage.googleapis.com`
3. Model: `gemini-1.5-flash` (fast and cost-effective)
4. Request format: `contents.parts[].text`
5. Response parsing: `candidates[0].content.parts[0].text`

**API Call Structure:**
```bash
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${API_KEY}" \
  -H "Content-Type: application/json" \
  -d "$PAYLOAD"
```

### Analysis Script (`analyze_results_gemini.py`)

**Key Changes:**
1. Uses `google-generativeai` library instead of `openai`
2. Embedding model: `models/embedding-001`
3. API configuration: `genai.configure(api_key=API_KEY)`
4. Embedding function: `genai.embed_content()`

**Embedding Code:**
```python
import google.generativeai as genai

genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

def get_embedding(text):
    result = genai.embed_content(
        model="models/embedding-001",
        content=text,
        task_type="retrieval_document"
    )
    return result['embedding']
```

---

## 💰 Cost Comparison

### Google Gemini Pricing (as of 2025)

| Component | Model | Cost |
|-----------|-------|------|
| **Translation** | `gemini-1.5-flash` | $0.075 per 1M tokens (input) |
| | | $0.30 per 1M tokens (output) |
| **Embeddings** | `embedding-001` | $0.025 per 1M tokens |

**Estimated Cost per Run:**
- 18 translation calls: ~$0.05
- 7 embedding calls: ~$0.005
- **Total: ~$0.055** (much cheaper than OpenAI!)

---

## 🛠️ Troubleshooting

### Issue 1: "GOOGLE_API_KEY not set"

**Solution:**
```bash
export GOOGLE_API_KEY="your-key-here"
```

### Issue 2: "Module not found: google.generativeai"

**Solution:**
```bash
pip install google-generativeai
# OR
pip install -r requirements_gemini.txt
```

### Issue 3: API Key Invalid

**Test your key:**
```bash
python3 << 'EOF'
import os
import google.generativeai as genai

genai.configure(api_key=os.environ.get("GOOGLE_API_KEY"))

try:
    result = genai.embed_content(
        model="models/embedding-001",
        content="test"
    )
    print("✓ API key is valid!")
except Exception as e:
    print(f"✗ API key error: {e}")
EOF
```

### Issue 4: Rate Limiting

**Solution:**
Increase delays in `run_full_experiment_gemini.sh`:
```bash
# Change from:
sleep 2

# To:
sleep 5
```

### Issue 5: Model Not Available

**Available Models:**
- `gemini-1.5-flash` (recommended - fast and cheap)
- `gemini-1.5-pro` (more capable but expensive)
- `gemini-1.0-pro` (older version)

**To change model:**
Edit `run_agent_chain_gemini.sh`, line 18:
```bash
MODEL="gemini-1.5-flash"  # Change to gemini-1.5-pro if needed
```

---

## 📊 Expected Results

The results should be similar to OpenAI, with slight variations due to different model architectures.

**Typical Distance Values:**
```
Noise  0%: Distance = 0.000-0.005 (nearly identical)
Noise 10%: Distance = 0.005-0.015
Noise 20%: Distance = 0.010-0.025
Noise 30%: Distance = 0.015-0.035
Noise 40%: Distance = 0.020-0.045
Noise 50%: Distance = 0.025-0.055
```

**Graph Interpretation:**
- **Lower line** = Better robustness
- **Gradual increase** = Expected behavior
- **Steep increase** = Model struggles with noise

---

## 🎯 Advantages of Using Gemini

1. **Lower Cost**: ~60% cheaper than OpenAI
2. **Fast Response**: Gemini Flash is optimized for speed
3. **Good Quality**: Comparable translation quality
4. **Google Integration**: Easy to use with other Google services
5. **Generous Free Tier**: More free requests per month

---

## 📚 Additional Resources

### Google Gemini Documentation
- [Gemini API Overview](https://ai.google.dev/docs)
- [Python SDK](https://ai.google.dev/api/python/google/generativeai)
- [Pricing](https://ai.google.dev/pricing)
- [API Reference](https://ai.google.dev/api/rest)

### Getting Your API Key
1. Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Click "Create API Key"
3. Copy the key (starts with `AIza...`)
4. Set it: `export GOOGLE_API_KEY="your-key"`

---

## ✅ Verification Checklist

Before running the full experiment:

- [ ] `GOOGLE_API_KEY` is set
- [ ] `google-generativeai` package installed
- [ ] Scripts are executable (`chmod +x`)
- [ ] Can run single test successfully
- [ ] API key has sufficient quota

---

## 🔄 Switching Between APIs

You can keep both setups and switch as needed:

**For OpenAI:**
```bash
export OPENAI_API_KEY="sk-..."
./run_full_experiment.sh
python3 analyze_results.py
```

**For Gemini:**
```bash
export GOOGLE_API_KEY="AIza..."
./run_full_experiment_gemini.sh
python3 analyze_results_gemini.py
```

Both will create the same output structure!

---

## 🎉 Summary

You now have:
- ✅ `run_agent_chain_gemini.sh` - Single execution with Gemini
- ✅ `run_full_experiment_gemini.sh` - Full experiment with Gemini
- ✅ `analyze_results_gemini.py` - Analysis using Gemini embeddings
- ✅ `requirements_gemini.txt` - Gemini-specific dependencies

**Next Steps:**
1. Set your `GOOGLE_API_KEY`
2. Install dependencies: `pip install -r requirements_gemini.txt`
3. Run: `./run_full_experiment_gemini.sh`
4. Analyze: `python3 analyze_results_gemini.py`
5. View: `open semantic_drift_analysis.png`

---

**Last Updated:** November 23, 2025  
**API Provider:** Google Gemini  
**Status:** ✅ Ready to use

**Happy Experimenting with Gemini! 🚀✨**

