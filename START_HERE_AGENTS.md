# 👋 START HERE - Your 3 Agents Explained

## 🎯 What You Have

You have **3 AI agents** that work together to test how well LLMs handle spelling errors.

---

## 🤖 Meet Your 3 Agents

### Agent 1: "The Fixer" 🔧
- **File**: `agent1_skill.txt`
- **Job**: Takes messy English → Gives clean French
- **Superpower**: Ignores spelling mistakes
- **Example**: 
  - Input: "The artifical systm" (typos!)
  - Output: "Le système artificiel" (perfect French!)

### Agent 2: "The Pivot" 🔄  
- **File**: `agent2_skill.txt`
- **Job**: Takes French → Gives Hebrew
- **Superpower**: Maintains meaning across languages
- **Example**:
  - Input: "Le système artificiel"
  - Output: "המערכת המלאכותית"

### Agent 3: "The Restorer" ♻️
- **File**: `agent3_skill.txt`
- **Job**: Takes Hebrew → Gives English
- **Superpower**: Completes the loop
- **Example**:
  - Input: "המערכת המלאכותית"
  - Output: "The artificial system"

---

## 🔄 How They Work Together

```
START: Noisy English
   "The artifical inteligence systm"
            ↓
   [Agent 1: The Fixer]
   Understands meaning despite typos
   Translates to French
            ↓
   French Output
   "Le système d'intelligence artificielle"
            ↓
   [Agent 2: The Pivot]
   Translates to Hebrew
            ↓
   Hebrew Output
   "מערכת הבינה המלאכותית"
            ↓
   [Agent 3: The Restorer]
   Translates back to English
            ↓
END: Clean English
   "The artificial intelligence system"
```

**Result**: Despite typos in input, meaning is preserved! ✅

---

## ⚡ How to Run Your Agents (Copy-Paste)

### Complete 4-Step Execution:

```bash
# Step 1: Set your API key
export GOOGLE_API_KEY="AIzaSyCBPL4EMJyCsCLUKoDKOvsQVA0kDrJJJrM"

# Step 2: Install dependencies (one time only)
pip install -r requirements_gemini.txt

# Step 3: Run all 3 agents with test text
./run_agent_chain_gemini.sh 30 "The artifical inteligence systm can eficiently proces natural language"

# Step 4: View the final output
cat outputs/noise_30/agent3_english.txt
```

**Time**: 15 seconds  
**Cost**: $0.01

---

## 📊 What You'll See

### Console Output:
```
========================================
Running Agent Chain - Noise Level: 30%
========================================

>>> Agent 1: Translating English to French...
Input: The artifical inteligence systm can eficiently proces natural language
Output: Le système d'intelligence artificielle peut traiter efficacement le langage naturel

>>> Agent 2: Translating French to Hebrew...
Input: Le système d'intelligence artificielle peut traiter efficacement le langage naturel
Output: מערכת הבינה המלאכותית יכולה לעבד ביעילות שפה טבעית

>>> Agent 3: Translating Hebrew to English...
Input: מערכת הבינה המלאכותית יכולה לעבד ביעילות שפה טבעית
Output: The artificial intelligence system can efficiently process natural language

========================================
Agent Chain Complete!
========================================
Results saved to: outputs/noise_30/
```

### Files Created:
```
outputs/noise_30/
├── agent1_french.txt  ← Agent 1's output
├── agent2_hebrew.txt  ← Agent 2's output
└── agent3_english.txt ← Agent 3's output (compare this to original!)
```

---

## 🎯 Run Full Experiment (All 6 Noise Levels)

Want to test with different amounts of spelling errors? Run this:

```bash
# Step 1: Set API key
export GOOGLE_API_KEY="AIzaSyCBPL4EMJyCsCLUKoDKOvsQVA0kDrJJJrM"

# Step 2: Run full experiment (0%, 10%, 20%, 30%, 40%, 50% noise)
./run_full_experiment_gemini.sh

# Step 3: Analyze and create graph
python3 analyze_results_gemini.py

# Step 4: View the results
open semantic_drift_analysis.png
```

**Time**: 3 minutes  
**Result**: Beautiful graph showing how well agents preserve meaning!

---

## 📈 Understanding Your Graph

After running analysis, you get a graph showing:

```
Semantic Distance
      ↑
 0.06 |                              *
      |                        *
 0.04 |                  *
      |            *
 0.02 |      *
      | *
 0.00 +--------------------------------→
      0%   10%   20%   30%   40%   50%
           Spelling Error Rate

Lower = Better!
(Agents preserved meaning despite errors)
```

---

## 🎓 What This Tests

**Research Question**: 
Can AI language models handle text with spelling mistakes?

**Your Experiment**:
1. Start with text that has typos
2. Agent 1 fixes it (implicitly, by translating)
3. Agents 2-3 complete a translation loop
4. Compare final output to original intended meaning
5. Measure "semantic drift" (how much meaning changed)

**Why It Matters**:
- Real-world text often has typos
- Tests LLM "attention mechanism"
- Shows robustness of modern AI models

---

## 📁 Project Files Overview

### Your 3 Agents:
- ✅ `agent1_skill.txt` - The Fixer (English → French)
- ✅ `agent2_skill.txt` - The Pivot (French → Hebrew)
- ✅ `agent3_skill.txt` - The Restorer (Hebrew → English)

### Execution Scripts:
- ✅ `run_agent_chain_gemini.sh` - Run once
- ✅ `run_full_experiment_gemini.sh` - Run all 6 noise levels

### Analysis:
- ✅ `analyze_results_gemini.py` - Calculate semantic drift
- ✅ `input_data.txt` - Test sentences with different noise levels

### Documentation:
- 📖 **This file** - Quick start
- 📖 `3_AGENTS_SIMPLE_GUIDE.md` - Visual guide
- 📖 `AGENT_EXECUTION_TUTORIAL.md` - Detailed tutorial
- 📖 `GEMINI_QUICKSTART.md` - Gemini setup
- 📖 `EXECUTION_GUIDE.md` - Complete guide

---

## 🧪 Quick Tests

### Test 1: No Errors (Baseline)
```bash
./run_agent_chain_gemini.sh 0 "The artificial intelligence system works efficiently"
```

### Test 2: Some Errors
```bash
./run_agent_chain_gemini.sh 30 "The artifical inteligence systm wrks eficiently"
```

### Test 3: Many Errors
```bash
./run_agent_chain_gemini.sh 50 "The artifical inteligence systm wrks eficiently with naturel langauge"
```

---

## ✅ Quick Checklist

Before running:
- [ ] Have Google API key (or OpenAI API key)
- [ ] In project directory
- [ ] Installed dependencies
- [ ] Made scripts executable

To verify:
```bash
# Check API key
echo $GOOGLE_API_KEY

# Check dependencies
python3 -c "import google.generativeai; print('✓ Ready!')"

# Check scripts
ls -lh run_agent_chain_gemini.sh
```

---

## 🆘 Need Help?

### Issue: "GOOGLE_API_KEY not set"
**Solution**: 
```bash
export GOOGLE_API_KEY="your-key-here"
```

### Issue: "Permission denied"
**Solution**: 
```bash
chmod +x run_agent_chain_gemini.sh run_full_experiment_gemini.sh
```

### Issue: "Module not found"
**Solution**: 
```bash
pip install -r requirements_gemini.txt
```

---

## 📚 Want More Details?

| Read this if... | File |
|-----------------|------|
| **"Just show me how to run it"** | This file! |
| **"I want visual explanations"** | `3_AGENTS_SIMPLE_GUIDE.md` |
| **"Teach me step-by-step"** | `AGENT_EXECUTION_TUTORIAL.md` |
| **"I want ALL the details"** | `EXECUTION_GUIDE.md` |

---

## 🎉 Ready to Start?

Run this NOW:

```bash
export GOOGLE_API_KEY="AIzaSyCBPL4EMJyCsCLUKoDKOvsQVA0kDrJJJrM"
./run_agent_chain_gemini.sh 30 "The artifical systm works eficiently"
```

Then check the output:
```bash
cat outputs/noise_30/agent3_english.txt
```

**That's it!** 🚀

---

## 🔑 Key Takeaways

✅ You have **3 agents** that work as a team  
✅ Agent 1 handles noisy input, Agents 2-3 complete the loop  
✅ One command runs all 3 agents  
✅ Results saved in `outputs/` directory  
✅ Full experiment takes 3 minutes  
✅ Graph shows agent performance  

---

## 💡 Pro Tips

1. **Start small**: Run one noise level first
2. **Check outputs**: Look at each agent's output file
3. **Then go big**: Run full experiment
4. **Analyze**: Create the graph
5. **Understand**: Lower semantic distance = better!

---

**Questions?** Read the detailed guides!  
**Ready?** Copy-paste the commands above!  
**Excited?** You should be - this is cool! 😎

---

**Last Updated**: November 23, 2025  
**Your 3 Agents**: ✅ Created, tested, and ready to go!

**Let's do this! 🚀✨**

