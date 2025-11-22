# 👋 START HERE - Agentic Turing Machine

## Welcome! 🎉

You have a complete implementation of the Agentic Turing Machine ready to run.

---

## ⚡ Super Quick Start (Copy & Paste)

```bash
# 1. Set your OpenAI API key (replace with your actual key)
export OPENAI_API_KEY='sk-your-key-here'

# 2. Install dependencies (one time only)
brew install jq  # macOS (or: apt-get install jq for Linux)
pip install -r requirements.txt

# 3. Verify setup
./verify_setup.sh

# 4. Run experiment
./run_full_experiment.sh

# 5. Analyze results
python3 analyze_results.py

# 6. View graph
open semantic_drift_analysis.png  # macOS
# or: xdg-open semantic_drift_analysis.png  # Linux
```

**Done!** 🎊

---

## 📖 What to Read Next?

Choose your path:

### 🏃‍♂️ I want to run it NOW
→ Read: **`QUICKSTART.md`**  
(5-minute setup guide)

### 📚 I want to understand everything
→ Read: **`README.md`**  
(Complete documentation)

### 🔍 I want to see the CLI commands
→ Read: **`CLI_EXECUTION_EXAMPLES.md`**  
(Detailed execution proof)

### ✅ I want to verify requirements
→ Read: **`DELIVERABLES.md`**  
(Complete checklist)

### 📊 I want a quick overview
→ Read: **`PROJECT_SUMMARY.md`**  
(One-page summary)

---

## 🎯 What This Project Does

Tests how well LLMs preserve meaning when text has spelling errors.

**Method**:
1. Take English sentence with typos
2. Translate: English → French → Hebrew → English
3. Compare original vs. final using AI embeddings
4. Repeat with different error rates (0% to 50%)
5. Graph the results

**Result**: Beautiful graph showing semantic drift vs. noise level

---

## 📁 File Guide

### Files You'll RUN
- `verify_setup.sh` - Check if ready ✓
- `run_full_experiment.sh` - Run experiment 🚀
- `analyze_results.py` - Create graph 📊

### Files You'll READ
- `START_HERE.md` - This file! 👋
- `QUICKSTART.md` - Fast path 🏃
- `README.md` - Full docs 📚
- `PROJECT_SUMMARY.md` - Overview 📊

### Files That Make It Work
- `agent1_skill.txt` - AI prompt #1
- `agent2_skill.txt` - AI prompt #2
- `agent3_skill.txt` - AI prompt #3
- `input_data.txt` - Test sentences
- `run_agent_chain.sh` - Core script
- `requirements.txt` - Python packages

---

## ⚠️ Before You Start

### Required:
1. ✅ OpenAI API key (starts with `sk-`)
2. ✅ Internet connection (for API calls)
3. ✅ Terminal/command line access
4. ✅ Python 3.7+ installed
5. ✅ 5 minutes of time

### Optional but helpful:
- Basic understanding of LLMs
- Familiarity with command line
- Understanding of embeddings/vectors

---

## 💰 Cost Estimate

Using OpenAI API:
- **Experiment** (18 API calls): ~$0.10
- **Analysis** (7 embedding calls): ~$0.005
- **Total**: Less than $0.15

Using `gpt-4o-mini` for cost efficiency.

---

## 🆘 Help!

### Script won't run?
```bash
chmod +x *.sh
```

### "jq not found"?
```bash
brew install jq  # macOS
# or
sudo apt-get install jq  # Linux
```

### "OPENAI_API_KEY not set"?
```bash
export OPENAI_API_KEY='your-key-here'
```

### Python packages missing?
```bash
pip install -r requirements.txt
```

### Still stuck?
1. Run: `./verify_setup.sh`
2. Read the error messages
3. Check `QUICKSTART.md` troubleshooting section

---

## 🎓 For Academic Submission

All requirements are met:
- ✅ CLI-only agent orchestration
- ✅ 3 sequential agents with system prompts
- ✅ 15+ word sentence
- ✅ 0-50% noise testing
- ✅ Python for analysis only
- ✅ Vector distance calculation
- ✅ Graph visualization
- ✅ Complete documentation

**Deliverables checklist**: See `DELIVERABLES.md`

---

## 🚀 Ready? Let's Go!

```bash
# Start here:
./verify_setup.sh
```

If all checks pass ✅, you're ready to run the experiment!

```bash
./run_full_experiment.sh
```

---

## 📊 What You'll Get

After running everything:

```
outputs/
├── noise_0/     (translations at 0% error)
├── noise_10/    (translations at 10% error)
├── noise_20/    (translations at 20% error)
├── noise_30/    (translations at 30% error)
├── noise_40/    (translations at 40% error)
└── noise_50/    (translations at 50% error)

semantic_drift_analysis.png   (pretty graph!)
semantic_drift_analysis.pdf   (for printing)
analysis_results.json         (raw data)
```

---

## 🎯 Success Looks Like

A graph with:
- **X-axis**: Error percentage (0% → 50%)
- **Y-axis**: Semantic distance
- **Line**: Shows how meaning drifts with noise

Lower distance = Better AI performance! 📈

---

## 📚 Documentation Tree

```
START_HERE.md ← You are here! 👋
│
├─ QUICKSTART.md (fast path, 5 min)
│
├─ README.md (everything you need to know)
│  ├─ Architecture
│  ├─ Installation
│  ├─ Usage
│  └─ Technical Details
│
├─ PROJECT_SUMMARY.md (one-page overview)
│
├─ CLI_EXECUTION_EXAMPLES.md (command reference)
│  ├─ Single execution examples
│  ├─ Full experiment flow
│  └─ Raw API interactions
│
└─ DELIVERABLES.md (requirements checklist)
   ├─ What's required
   ├─ What you have
   └─ How to verify
```

---

## 🎉 Have Fun!

This project is a hands-on exploration of:
- 🤖 Multi-agent AI systems
- 🧠 Attention mechanisms
- 📊 Semantic analysis
- 💻 CLI automation

Enjoy watching AI handle chaos! ✨

---

**Questions?** Check the README.md for detailed explanations.

**Ready to start?** Run: `./verify_setup.sh`

**Good luck!** 🍀


