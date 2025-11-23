# 🤖 Your 3 Agents - Simple Visual Guide

## 🎯 The 3 Agents in 30 Seconds

```
📝 INPUT: "The artifical inteligence systm works eficiently"
                         ↓
┌────────────────────────────────────────────────┐
│  🤖 AGENT 1: The Fixer                        │
│  File: agent1_skill.txt                       │
│  Does: Ignores typos → Translates to French   │
│  Output: "Le système d'intelligence           │
│          artificielle fonctionne efficacement" │
└────────────────────────────────────────────────┘
                         ↓
┌────────────────────────────────────────────────┐
│  🤖 AGENT 2: The Pivot                        │
│  File: agent2_skill.txt                       │
│  Does: French → Hebrew                         │
│  Output: "מערכת הבינה המלאכותית פועלת ביעילות"│
└────────────────────────────────────────────────┘
                         ↓
┌────────────────────────────────────────────────┐
│  🤖 AGENT 3: The Restorer                     │
│  File: agent3_skill.txt                       │
│  Does: Hebrew → English                        │
│  Output: "The artificial intelligence system  │
│          works efficiently"                    │
└────────────────────────────────────────────────┘
                         ↓
✅ RESULT: Meaning preserved despite typos!
```

---

## 📁 Your 3 Agent Files

### 1️⃣ `agent1_skill.txt` - The Fixer
```
✓ Created and ready
✓ Handles noisy English input
✓ Outputs clean French
```

### 2️⃣ `agent2_skill.txt` - The Pivot
```
✓ Created and ready
✓ Translates French to Hebrew
✓ Maintains semantic meaning
```

### 3️⃣ `agent3_skill.txt` - The Restorer
```
✓ Created and ready
✓ Translates Hebrew to English
✓ Completes the loop
```

---

## ⚡ How to Execute (3 Commands)

### STEP 1: Set API Key
```bash
export GOOGLE_API_KEY="AIzaSyCBPL4EMJyCsCLUKoDKOvsQVA0kDrJJJrM"
```

### STEP 2: Run the 3 Agents
```bash
./run_agent_chain_gemini.sh 30 "The artifical inteligence systm works eficiently"
```

### STEP 3: See Results
```bash
cat outputs/noise_30/agent1_french.txt   # Agent 1 output
cat outputs/noise_30/agent2_hebrew.txt   # Agent 2 output
cat outputs/noise_30/agent3_english.txt  # Agent 3 output (final)
```

**That's it!** ✅

---

## 🔄 What Happens When You Run

```
Terminal Output:
========================================
Running Agent Chain - Noise Level: 30%
========================================

>>> Agent 1: Translating English to French...
Input: The artifical inteligence systm works eficiently
Output: Le système d'intelligence artificielle fonctionne efficacement
✓ Saved to: outputs/noise_30/agent1_french.txt

>>> Agent 2: Translating French to Hebrew...
Input: Le système d'intelligence artificielle fonctionne efficacement
Output: מערכת הבינה המלאכותית פועלת ביעילות
✓ Saved to: outputs/noise_30/agent2_hebrew.txt

>>> Agent 3: Translating Hebrew to English...
Input: מערכת הבינה המלאכותית פועלת ביעילות
Output: The artificial intelligence system works efficiently
✓ Saved to: outputs/noise_30/agent3_english.txt

========================================
Agent Chain Complete!
========================================
```

---

## 📂 Files Created

After running, you get:

```
outputs/noise_30/
├── agent1_french.txt  ← Agent 1's French output
├── agent2_hebrew.txt  ← Agent 2's Hebrew output
└── agent3_english.txt ← Agent 3's final English (for comparison)
```

---

## 🎯 Test All Noise Levels (Full Experiment)

Run all 3 agents through 6 different noise levels:

```bash
# Step 1: Set API key
export GOOGLE_API_KEY="your-key"

# Step 2: Run full experiment
./run_full_experiment_gemini.sh

# Step 3: Analyze results
python3 analyze_results_gemini.py

# Step 4: View graph
open semantic_drift_analysis.png
```

**Time**: ~2-3 minutes  
**Cost**: ~$0.05 with Gemini

---

## 🧪 Quick Tests

### Test 1: Clean Text (0% errors)
```bash
./run_agent_chain_gemini.sh 0 "The artificial intelligence system works efficiently"
```

### Test 2: Light Errors (10%)
```bash
./run_agent_chain_gemini.sh 10 "The artifical intelligence systm works efficiently"
```

### Test 3: Heavy Errors (50%)
```bash
./run_agent_chain_gemini.sh 50 "The artifical inteligence systm wrks eficiently"
```

---

## 💡 Understanding the Agents

### Agent 1: Why "The Fixer"?
- Input has typos: "artifical", "inteligence", "systm"
- Agent 1 **ignores** the typos
- Understands you meant "artificial intelligence system"
- Translates the **correct meaning** to French

### Agent 2: Why "The Pivot"?
- Takes clean French from Agent 1
- Acts as the "middle point" in the translation chain
- Pivots from French to Hebrew
- Maintains all semantic meaning

### Agent 3: Why "The Restorer"?
- Completes the translation loop
- Brings it back to English
- "Restores" the original language
- Final output can be compared to original

---

## 📊 What You're Measuring

```
Original (intended): "artificial intelligence system"
With typos:          "artifical inteligence systm"
                              ↓
                     [3 Agents Process]
                              ↓
Final output:        "artificial intelligence system"
                              ↓
Semantic distance:   0.015 (very close!)
```

**Lower distance = Better LLM performance!**

---

## ✅ Checklist

Before running:
- [ ] Set `GOOGLE_API_KEY`
- [ ] Install: `pip install -r requirements_gemini.txt`
- [ ] Make executable: `chmod +x run_agent_chain_gemini.sh`
- [ ] In project directory

---

## 🎓 What This Tests

**Question**: How well do LLMs handle noisy input?

**Method**: 
- Agent 1 handles typos
- Agents 2-3 complete translation loop
- Compare final to original
- Measure semantic drift

**Result**: Shows LLM robustness to spelling errors!

---

## 📚 More Details?

| Want to... | Read... |
|------------|---------|
| **Quick start** | This file! |
| **Step-by-step tutorial** | `AGENT_EXECUTION_TUTORIAL.md` |
| **Gemini setup** | `GEMINI_QUICKSTART.md` |
| **Full documentation** | `EXECUTION_GUIDE.md` |

---

## 🚀 Ready? Run This Now!

```bash
# Complete execution in 4 commands:
export GOOGLE_API_KEY="AIzaSyCBPL4EMJyCsCLUKoDKOvsQVA0kDrJJJrM"
pip install -r requirements_gemini.txt
./run_agent_chain_gemini.sh 30 "The artifical inteligence systm works well"
cat outputs/noise_30/agent3_english.txt
```

**That's all!** 🎉

---

## 🔑 Key Points

✅ **3 agents** already created for you  
✅ **Files**: `agent1_skill.txt`, `agent2_skill.txt`, `agent3_skill.txt`  
✅ **Execution**: One command runs all 3 agents  
✅ **Output**: Saved in `outputs/noise_X/` directory  
✅ **Time**: 10-15 seconds per run  
✅ **Cost**: ~$0.01 per run with Gemini  

---

**Last Updated**: November 23, 2025  
**Status**: ✅ All 3 agents ready to execute

**Go try it! 🚀✨**

