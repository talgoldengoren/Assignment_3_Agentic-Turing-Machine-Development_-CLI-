# 🎓 Project Summary: Agentic Turing Machine (CLI)

## 📊 What This Project Does

This project implements a **3-agent translation pipeline** to test how well Large Language Models can preserve semantic meaning when processing noisy (misspelled) text through multiple translation steps.

### The Journey
```
English (with typos) → French → Hebrew → English (clean)
```

### The Question
**How much semantic meaning is lost when text contains spelling errors?**

The answer is quantified using **vector embeddings** and **cosine distance** metrics.

---

## 🚀 Quick Start (3 Commands)

```bash
# 1. Verify everything is ready
./verify_setup.sh

# 2. Run the full experiment (all noise levels)
./run_full_experiment.sh

# 3. Analyze and generate graph
python3 analyze_results.py
```

**Time**: ~3-5 minutes total  
**API Calls**: ~18 calls (6 noise levels × 3 agents)  
**Output**: Graphs + detailed JSON results

---

## 📁 Project Files (13 Total)

### 🎯 Core Execution Files (7)
| File | Purpose | Type |
|------|---------|------|
| `run_agent_chain.sh` | Execute single noise level | CLI Script |
| `run_full_experiment.sh` | Run all noise levels (0%-50%) | CLI Script |
| `analyze_results.py` | Calculate embeddings & generate graph | Python |
| `agent1_skill.txt` | System prompt for English→French | Config |
| `agent2_skill.txt` | System prompt for French→Hebrew | Config |
| `agent3_skill.txt` | System prompt for Hebrew→English | Config |
| `input_data.txt` | Original + noisy sentences | Data |

### 📚 Documentation Files (5)
| File | Purpose |
|------|---------|
| `README.md` | Complete project documentation |
| `QUICKSTART.md` | 5-minute setup guide |
| `CLI_EXECUTION_EXAMPLES.md` | Detailed CLI command examples |
| `DELIVERABLES.md` | Requirements checklist |
| `PROJECT_SUMMARY.md` | This file - quick overview |

### 🛠️ Helper Files (2)
| File | Purpose |
|------|---------|
| `verify_setup.sh` | Check if setup is complete |
| `requirements.txt` | Python dependencies |

---

## 🎯 The Three Agents

### Agent 1: The Fixer/Filter 🔧
- **Input**: English text with spelling errors
- **Skill**: Ignore typos, infer meaning
- **Output**: Clean, grammatical French

### Agent 2: The Pivot 🔄
- **Input**: French text
- **Skill**: Accurate translation
- **Output**: Fluent Hebrew

### Agent 3: The Restorer ✨
- **Input**: Hebrew text
- **Skill**: Complete the loop
- **Output**: Reconstructed English

---

## 📊 The Experiment

### Test Sentence (16 words)
> "The artificial intelligence system can efficiently process natural language and understand complex semantic relationships within textual data."

### Noise Levels Tested
- **0%** - Clean (baseline)
- **10%** - 2 misspelled words
- **20%** - 3 misspelled words
- **30%** - 5 misspelled words
- **40%** - 6 misspelled words
- **50%** - 8 misspelled words

### What We Measure
**Cosine Distance** between:
- Original clean sentence embedding
- Final reconstructed sentence embedding

**Lower distance** = Better semantic preservation 🎯

---

## 🔬 Technical Stack

### CLI Orchestration (NO Python!)
- **Bash** - Shell scripting
- **curl** - HTTP API requests
- **jq** - JSON parsing
- **OpenAI API** - LLM capabilities

### Python Analysis (Data Science)
- **openai** - Embeddings API
- **numpy** - Numerical operations
- **matplotlib** - Visualization
- **scikit-learn** - Cosine similarity

---

## 📤 Deliverables Generated

### During Experiment
```
outputs/
├── noise_0/  
│   ├── agent1_french.txt
│   ├── agent2_hebrew.txt
│   └── agent3_english.txt
├── noise_10/ [same structure]
├── noise_20/ [same structure]
├── noise_30/ [same structure]
├── noise_40/ [same structure]
└── noise_50/ [same structure]
```

### After Analysis
- `semantic_drift_analysis.png` - Visualization (PNG)
- `semantic_drift_analysis.pdf` - High-quality vector graph
- `analysis_results.json` - Detailed numerical results

---

## 💡 Key Insights

### What This Demonstrates

1. **LLM Robustness**: How well attention mechanisms handle noise
2. **Multi-Agent Systems**: Sequential agent orchestration patterns
3. **Semantic Preservation**: Quantifying meaning across transformations
4. **CLI Automation**: Pure shell scripting for AI workflows

### Expected Results

**Hypothesis**: Modern LLMs should demonstrate strong robustness
- Low noise (0-20%): Minimal drift
- Medium noise (30-40%): Slight increase
- High noise (50%): Measurable but bounded drift

The graph will reveal whether the attention mechanism successfully filters noise across multiple transformations.

---

## 🎓 Academic Requirements ✅

| Requirement | Status | Evidence |
|-------------|--------|----------|
| CLI-only orchestration | ✅ | `run_agent_chain.sh`, `run_full_experiment.sh` |
| NO Python for agents | ✅ | Pure bash + curl + jq |
| 3 sequential agents | ✅ | `agent1_skill.txt`, `agent2_skill.txt`, `agent3_skill.txt` |
| 15+ word sentence | ✅ | 16 words in `input_data.txt` |
| 25%+ initial noise | ✅ | 50% variant has 50% errors |
| 0-50% noise range | ✅ | 0%, 10%, 20%, 30%, 40%, 50% |
| Python for analysis | ✅ | `analyze_results.py` |
| Vector distance calc | ✅ | Cosine distance with embeddings |
| Graph visualization | ✅ | Generated PNG/PDF |

---

## 🚦 Status Check

Run this to verify everything is ready:
```bash
./verify_setup.sh
```

Expected output:
```
✓ jq found
✓ curl found
✓ Python 3 found
✓ OPENAI_API_KEY set
✓ Python packages installed
✓ All required files present
✓ Scripts executable

✓ ALL CHECKS PASSED!
```

---

## 📚 Where to Look

### New to the project?
Start here: **`QUICKSTART.md`**

### Need complete documentation?
Read: **`README.md`**

### Want to see exact CLI commands?
Check: **`CLI_EXECUTION_EXAMPLES.md`**

### Verifying requirements?
Review: **`DELIVERABLES.md`**

### Quick overview?
You're reading it! **`PROJECT_SUMMARY.md`**

---

## 🎯 Success Criteria

You'll know the project is working when:

1. ✅ `./verify_setup.sh` passes all checks
2. ✅ `./run_full_experiment.sh` completes without errors
3. ✅ `outputs/` directory contains 6 subdirectories with 3 files each
4. ✅ `python3 analyze_results.py` generates graphs
5. ✅ Graph shows noise % on X-axis, distance on Y-axis
6. ✅ Results make intuitive sense (higher noise → higher distance)

---

## 🔍 Architecture at a Glance

```
┌─────────────────────────────────────────────────┐
│           PROJECT STRUCTURE                     │
├─────────────────────────────────────────────────┤
│                                                 │
│  INPUT                                          │
│  └─ input_data.txt (clean + noisy sentences)   │
│                                                 │
│  CONFIGURATION                                  │
│  ├─ agent1_skill.txt (English→French)          │
│  ├─ agent2_skill.txt (French→Hebrew)           │
│  └─ agent3_skill.txt (Hebrew→English)          │
│                                                 │
│  EXECUTION (CLI - NO PYTHON)                    │
│  ├─ run_agent_chain.sh (single run)            │
│  └─ run_full_experiment.sh (all noise levels)  │
│      │                                          │
│      └──→ Uses: bash + curl + jq               │
│                                                 │
│  ANALYSIS (PYTHON ONLY)                         │
│  └─ analyze_results.py                          │
│      │                                          │
│      └──→ Uses: openai + numpy + matplotlib    │
│                                                 │
│  OUTPUT                                         │
│  ├─ outputs/ (intermediate translations)       │
│  ├─ semantic_drift_analysis.png (graph)        │
│  └─ analysis_results.json (data)               │
│                                                 │
│  DOCUMENTATION                                  │
│  ├─ README.md (comprehensive)                  │
│  ├─ QUICKSTART.md (fast start)                 │
│  ├─ CLI_EXECUTION_EXAMPLES.md (proof)          │
│  ├─ DELIVERABLES.md (checklist)                │
│  └─ PROJECT_SUMMARY.md (this file)             │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## 🎉 Final Notes

This project demonstrates:
- ✨ Multi-agent orchestration
- 🧠 LLM attention mechanism testing
- 📊 Quantitative semantic analysis
- 💻 CLI automation skills
- 🐍 Python data science capabilities

**Total Implementation**:
- 13 files
- ~1,000 lines of documentation
- ~400 lines of code
- 3 agents
- 6 experiments
- 1 comprehensive analysis

**Ready to test the robustness of AI?** 🚀

```bash
./verify_setup.sh && ./run_full_experiment.sh && python3 analyze_results.py
```

---

**Created**: November 22, 2025  
**Purpose**: Task 3 - Agentic Turing Machine Development (CLI)  
**Status**: ✅ Complete and ready for execution


