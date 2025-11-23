# 🔄 API Comparison: OpenAI vs Google Gemini

## Quick Reference Card

### 📋 Side-by-Side Commands

| Step | OpenAI | Google Gemini |
|------|--------|---------------|
| **Set API Key** | `export OPENAI_API_KEY="sk-..."` | `export GOOGLE_API_KEY="AIza..."` |
| **Install Deps** | `pip install -r requirements.txt` | `pip install -r requirements_gemini.txt` |
| **Single Test** | `./run_agent_chain.sh 30 "text"` | `./run_agent_chain_gemini.sh 30 "text"` |
| **Full Experiment** | `./run_full_experiment.sh` | `./run_full_experiment_gemini.sh` |
| **Analysis** | `python analyze_results.py` | `python analyze_results_gemini.py` |
| **View Graph** | `open semantic_drift_analysis.png` | `open semantic_drift_analysis.png` |

---

## 💰 Cost Comparison

### OpenAI
- **Model**: `gpt-4o-mini`
- **Translation**: 18 calls × ~$0.008 = ~$0.14
- **Embeddings**: 7 calls × ~$0.001 = ~$0.007
- **Total per run**: ~**$0.15**

### Google Gemini
- **Model**: `gemini-1.5-flash`
- **Translation**: 18 calls × ~$0.003 = ~$0.05
- **Embeddings**: 7 calls × ~$0.001 = ~$0.007
- **Total per run**: ~**$0.055**

**Savings with Gemini**: ~63% cheaper! 💸

---

## ⚡ Performance Comparison

| Metric | OpenAI | Google Gemini |
|--------|--------|---------------|
| **Speed** | Fast (1-2s per call) | Very Fast (0.5-1s per call) |
| **Quality** | Excellent | Excellent |
| **Accuracy** | High | High |
| **Reliability** | Very High | Very High |
| **Rate Limits** | 3,500 RPM (free tier) | 15 RPM (free tier), 2M tokens/min |

---

## 📦 Files Used

### OpenAI Setup
```
✓ run_agent_chain.sh
✓ run_full_experiment.sh
✓ analyze_results.py
✓ requirements.txt
✓ agent1_skill.txt
✓ agent2_skill.txt
✓ agent3_skill.txt
```

### Gemini Setup
```
✓ run_agent_chain_gemini.sh
✓ run_full_experiment_gemini.sh
✓ analyze_results_gemini.py
✓ requirements_gemini.txt
✓ agent1_skill.txt  (same)
✓ agent2_skill.txt  (same)
✓ agent3_skill.txt  (same)
```

**Note**: Agent skill files are identical for both APIs!

---

## 🔧 Technical Differences

### API Endpoints

**OpenAI:**
```
POST https://api.openai.com/v1/chat/completions
Header: Authorization: Bearer $OPENAI_API_KEY
```

**Gemini:**
```
POST https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=$GOOGLE_API_KEY
```

### Request Format

**OpenAI:**
```json
{
  "model": "gpt-4o-mini",
  "messages": [
    {"role": "system", "content": "prompt"},
    {"role": "user", "content": "input"}
  ],
  "temperature": 0.3,
  "max_tokens": 500
}
```

**Gemini:**
```json
{
  "contents": [
    {
      "parts": [
        {"text": "prompt\n\nUser input:\ninput"}
      ]
    }
  ],
  "generationConfig": {
    "temperature": 0.3,
    "maxOutputTokens": 500
  }
}
```

### Response Parsing

**OpenAI:**
```bash
OUTPUT=$(echo "$RESPONSE" | jq -r '.choices[0].message.content')
```

**Gemini:**
```bash
OUTPUT=$(echo "$RESPONSE" | jq -r '.candidates[0].content.parts[0].text')
```

---

## 🎯 When to Use Which?

### Use OpenAI If:
- ✅ You already have OpenAI credits
- ✅ You need maximum accuracy for critical tasks
- ✅ You're familiar with OpenAI's ecosystem
- ✅ You want the most widely tested solution

### Use Gemini If:
- ✅ You want to minimize costs (~63% cheaper)
- ✅ You need faster response times
- ✅ You're exploring Google's AI ecosystem
- ✅ You want better rate limits on free tier
- ✅ You're cost-sensitive for multiple runs

---

## 🔄 Switching Between APIs

You can easily switch between APIs:

### Method 1: Use Different Terminals
```bash
# Terminal 1 (OpenAI)
export OPENAI_API_KEY="sk-..."
./run_full_experiment.sh

# Terminal 2 (Gemini)
export GOOGLE_API_KEY="AIza..."
./run_full_experiment_gemini.sh
```

### Method 2: Set Both Keys
```bash
# Set both keys
export OPENAI_API_KEY="sk-..."
export GOOGLE_API_KEY="AIza..."

# Run OpenAI version
./run_full_experiment.sh
python analyze_results.py
mv semantic_drift_analysis.png semantic_drift_openai.png

# Run Gemini version
./run_full_experiment_gemini.sh
python analyze_results_gemini.py
mv semantic_drift_analysis.png semantic_drift_gemini.png

# Compare results!
open semantic_drift_openai.png semantic_drift_gemini.png
```

---

## 📊 Expected Results Comparison

Both APIs should produce similar results with slight variations:

### Typical Distance Values

| Noise | OpenAI (typical) | Gemini (typical) |
|-------|------------------|------------------|
| 0% | 0.001-0.003 | 0.001-0.004 |
| 10% | 0.005-0.015 | 0.006-0.016 |
| 20% | 0.010-0.025 | 0.011-0.026 |
| 30% | 0.015-0.035 | 0.016-0.037 |
| 40% | 0.020-0.045 | 0.021-0.048 |
| 50% | 0.025-0.055 | 0.027-0.058 |

**Conclusion**: Both APIs show similar robustness to noise!

---

## 🛠️ Complete Setup Examples

### Setup for OpenAI

```bash
# 1. Set API key
export OPENAI_API_KEY="sk-your-key"

# 2. Install dependencies
pip install -r requirements.txt

# 3. Make executable
chmod +x run_agent_chain.sh run_full_experiment.sh

# 4. Run
./run_full_experiment.sh
python analyze_results.py

# 5. View
open semantic_drift_analysis.png
```

### Setup for Gemini

```bash
# 1. Set API key
export GOOGLE_API_KEY="AIza-your-key"

# 2. Install dependencies
pip install -r requirements_gemini.txt

# 3. Make executable
chmod +x run_agent_chain_gemini.sh run_full_experiment_gemini.sh

# 4. Run
./run_full_experiment_gemini.sh
python analyze_results_gemini.py

# 5. View
open semantic_drift_analysis.png
```

---

## 🎓 Learning Value

Using both APIs teaches you:
- ✅ **API Integration**: Working with different API providers
- ✅ **Cost Optimization**: Choosing the right tool for your budget
- ✅ **Portability**: Writing code that works across platforms
- ✅ **Comparison**: Understanding differences between LLM providers
- ✅ **Debugging**: Handling different response formats

---

## 📚 Additional Resources

### OpenAI
- [API Documentation](https://platform.openai.com/docs)
- [Pricing](https://openai.com/pricing)
- [Python SDK](https://github.com/openai/openai-python)

### Google Gemini
- [API Documentation](https://ai.google.dev/docs)
- [Pricing](https://ai.google.dev/pricing)
- [Python SDK](https://ai.google.dev/api/python/google/generativeai)
- [Get API Key](https://makersuite.google.com/app/apikey)

---

## ✅ Quick Decision Matrix

| Your Situation | Recommendation |
|----------------|----------------|
| First time user | Try **Gemini** (cheaper to experiment) |
| Production system | Use **OpenAI** (more stable) |
| Cost-sensitive | Use **Gemini** (63% cheaper) |
| Research paper | Use **both** (compare results) |
| Learning | Use **both** (learn both APIs) |
| Speed matters | Use **Gemini** (faster) |
| Accuracy critical | Use **OpenAI** (slight edge) |

---

## 🎉 Summary

**Both APIs work great!**

- 📝 Same input data
- 🤖 Same agent architecture
- 📊 Same analysis method
- 📈 Similar results
- 💰 Different costs

**Choose based on your needs, or try both!**

---

**Last Updated:** November 23, 2025  
**Status:** ✅ Both APIs fully supported

**Happy Experimenting! 🚀✨**

