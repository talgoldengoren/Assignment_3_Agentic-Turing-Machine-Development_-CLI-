# 🤖 3-Agent System: Complete Execution Tutorial

## 📋 Overview

This tutorial shows you **exactly** what the 3 agents are, how they work, and how to execute them step-by-step.

---

## 🎯 The 3 Agents Explained

### 🤖 Agent 1: The Fixer/Filter

**Location**: `agent1_skill.txt`

**Role**: English (with spelling errors) → French

**What it does**:
- Receives English text that may have spelling mistakes
- **Ignores** the typos and figures out what you meant
- Translates the **intended meaning** to perfect French
- Outputs only the French translation

**Example**:
```
Input:  "The artifical inteligence systm works well"
        ↓ (understands you meant "artificial intelligence system")
Output: "Le système d'intelligence artificielle fonctionne bien"
```

**The Skill/Prompt**:
```text
You are Agent 1: The Fixer/Filter.

Your role is to translate English text to French, with a special 
capability to handle noisy input.

CRITICAL INSTRUCTIONS:
1. The input text may contain spelling errors and typos
2. You must IGNORE the spelling mistakes and focus on inferring 
   the correct intended meaning
3. DO NOT correct the spelling - simply understand what the user 
   meant to say
4. Translate the INTENDED meaning into grammatically correct, 
   fluent French
5. Produce only the French translation - no explanations, 
   no corrections, no commentary
```

---

### 🤖 Agent 2: The Pivot

**Location**: `agent2_skill.txt`

**Role**: French → Hebrew

**What it does**:
- Receives clean French text from Agent 1
- Translates it to Hebrew
- Maintains all semantic meaning
- Outputs only the Hebrew translation

**Example**:
```
Input:  "Le système d'intelligence artificielle fonctionne bien"
        ↓ (translates to Hebrew)
Output: "מערכת הבינה המלאכותית עובדת היטב"
```

**The Skill/Prompt**:
```text
You are Agent 2: The Pivot.

Your role is to translate French text into Hebrew with high accuracy.

CRITICAL INSTRUCTIONS:
1. You will receive French text as input
2. Translate it directly into fluent, grammatically correct Hebrew
3. Maintain the semantic meaning and nuance from the French
4. Use natural Hebrew phrasing and grammar
5. Produce only the Hebrew translation - no explanations, no commentary
```

---

### 🤖 Agent 3: The Restorer

**Location**: `agent3_skill.txt`

**Role**: Hebrew → English

**What it does**:
- Receives Hebrew text from Agent 2
- Translates it back to English
- Completes the translation loop
- Outputs only the English translation

**Example**:
```
Input:  "מערכת הבינה המלאכותית עובדת היטב"
        ↓ (translates back to English)
Output: "The artificial intelligence system works well"
```

**The Skill/Prompt**:
```text
You are Agent 3: The Restorer.

Your role is to translate Hebrew text back into English, completing 
the translation loop.

CRITICAL INSTRUCTIONS:
1. You will receive Hebrew text as input
2. Translate it into clear, grammatically correct English
3. Maintain all semantic meaning and nuance from the Hebrew
4. Use natural English phrasing and grammar
5. Produce only the English translation - no explanations, no commentary
```

---

## 🔄 How They Work Together

```
┌─────────────────────────────────────────────────────────┐
│  INPUT: Noisy English                                   │
│  "The artifical inteligence systm works eficiently"     │
└─────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────┐
│  AGENT 1: The Fixer                                     │
│  • Ignores spelling errors                              │
│  • Understands: "artificial intelligence system         │
│    works efficiently"                                   │
│  • Translates to French                                 │
└─────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────┐
│  FRENCH OUTPUT                                          │
│  "Le système d'intelligence artificielle fonctionne     │
│   efficacement"                                         │
└─────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────┐
│  AGENT 2: The Pivot                                     │
│  • Takes French text                                    │
│  • Translates to Hebrew                                 │
│  • Maintains meaning                                    │
└─────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────┐
│  HEBREW OUTPUT                                          │
│  "מערכת הבינה המלאכותית פועלת ביעילות"                │
└─────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────┐
│  AGENT 3: The Restorer                                  │
│  • Takes Hebrew text                                    │
│  • Translates back to English                           │
│  • Completes the loop                                   │
└─────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────┐
│  FINAL ENGLISH OUTPUT                                   │
│  "The artificial intelligence system works efficiently" │
└─────────────────────────────────────────────────────────┘
                         ↓
┌─────────────────────────────────────────────────────────┐
│  COMPARISON                                             │
│  Original (intended): "artificial intelligence system"  │
│  Final: "artificial intelligence system"                │
│  ✅ Meaning preserved!                                  │
└─────────────────────────────────────────────────────────┘
```

---

## 🚀 How to Execute the Agents

You have **3 ways** to execute the agents:

---

## 📍 METHOD 1: Automated Execution (EASIEST)

### Step 1: Choose Your API

**Option A: Using Google Gemini (Recommended - Cheaper)**
```bash
# Set your API key
export GOOGLE_API_KEY="AIzaSyCBPL4EMJyCsCLUKoDKOvsQVA0kDrJJJrM"
```

**Option B: Using OpenAI**
```bash
# Set your API key
export OPENAI_API_KEY="sk-your-key-here"
```

### Step 2: Run a Single Test

**With Gemini:**
```bash
./run_agent_chain_gemini.sh 30 "The artifical inteligence systm can eficiently proces natural langauge and understnd complex semantic relationships within textual data."
```

**With OpenAI:**
```bash
./run_agent_chain.sh 30 "The artifical inteligence systm can eficiently proces natural langauge and understnd complex semantic relationships within textual data."
```

### Step 3: Watch the Agents Execute

**You'll see:**
```
========================================
Running Agent Chain - Noise Level: 30%
========================================

>>> Agent 1: Translating English to French...
Input: The artifical inteligence systm can eficiently...
Output: Le système d'intelligence artificielle peut efficacement...

>>> Agent 2: Translating French to Hebrew...
Input: Le système d'intelligence artificielle peut efficacement...
Output: מערכת הבינה המלאכותית יכולה ביעילות...

>>> Agent 3: Translating Hebrew to English...
Input: מערכת הבינה המלאכותית יכולה ביעילות...
Output: The artificial intelligence system can efficiently...

========================================
Agent Chain Complete!
========================================
```

### Step 4: Check the Results

```bash
# View all outputs for this noise level
ls outputs/noise_30/

# You'll see:
# agent1_french.txt  - Agent 1's French output
# agent2_hebrew.txt  - Agent 2's Hebrew output
# agent3_english.txt - Agent 3's final English output

# View each file
cat outputs/noise_30/agent1_french.txt
cat outputs/noise_30/agent2_hebrew.txt
cat outputs/noise_30/agent3_english.txt
```

---

## 📍 METHOD 2: Manual Step-by-Step Execution

This method shows you **exactly** how the agents work internally.

### Step 1: Set Up Environment

```bash
# Navigate to project
cd "/Users/fouadaz/LearningFromUniversity/Learning/LLMSAndMultiAgentOrchestration/course-materials/assignments/Assignment_3_Agentic Turing Machine Development_(CLI)"

# Set API key (choose one)
export GOOGLE_API_KEY="your-key"
# OR
export OPENAI_API_KEY="your-key"

# Create output directory
mkdir -p outputs/manual_test
```

### Step 2: Execute Agent 1 Manually

#### For Gemini:
```bash
# Define your noisy English input
INPUT_TEXT="The artifical systm works eficiently"

# Read Agent 1's skill/prompt
AGENT1_SKILL=$(cat agent1_skill.txt)

# Create the API request
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${GOOGLE_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "{
    \"contents\": [{
      \"parts\": [{
        \"text\": \"${AGENT1_SKILL}\\n\\nUser input:\\n${INPUT_TEXT}\"
      }]
    }],
    \"generationConfig\": {
      \"temperature\": 0.3,
      \"maxOutputTokens\": 500
    }
  }" | jq -r '.candidates[0].content.parts[0].text' > outputs/manual_test/agent1_french.txt

# View Agent 1's output
echo "=== AGENT 1 OUTPUT (French) ==="
cat outputs/manual_test/agent1_french.txt
```

#### For OpenAI:
```bash
# Define your noisy English input
INPUT_TEXT="The artifical systm works eficiently"

# Read Agent 1's skill/prompt
AGENT1_SKILL=$(cat agent1_skill.txt)

# Create the API request
curl -s -X POST "https://api.openai.com/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer ${OPENAI_API_KEY}" \
  -d "{
    \"model\": \"gpt-4o-mini\",
    \"messages\": [
      {\"role\": \"system\", \"content\": \"${AGENT1_SKILL}\"},
      {\"role\": \"user\", \"content\": \"${INPUT_TEXT}\"}
    ],
    \"temperature\": 0.3,
    \"max_tokens\": 500
  }" | jq -r '.choices[0].message.content' > outputs/manual_test/agent1_french.txt

# View Agent 1's output
echo "=== AGENT 1 OUTPUT (French) ==="
cat outputs/manual_test/agent1_french.txt
```

### Step 3: Execute Agent 2 Manually

```bash
# Read Agent 1's output (French)
FRENCH_TEXT=$(cat outputs/manual_test/agent1_french.txt)

# Read Agent 2's skill
AGENT2_SKILL=$(cat agent2_skill.txt)

# For Gemini:
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${GOOGLE_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "{
    \"contents\": [{
      \"parts\": [{
        \"text\": \"${AGENT2_SKILL}\\n\\nUser input:\\n${FRENCH_TEXT}\"
      }]
    }],
    \"generationConfig\": {
      \"temperature\": 0.3,
      \"maxOutputTokens\": 500
    }
  }" | jq -r '.candidates[0].content.parts[0].text' > outputs/manual_test/agent2_hebrew.txt

# For OpenAI:
# curl -s -X POST "https://api.openai.com/v1/chat/completions" \
#   -H "Content-Type: application/json" \
#   -H "Authorization: Bearer ${OPENAI_API_KEY}" \
#   -d "{...}" | jq -r '.choices[0].message.content' > outputs/manual_test/agent2_hebrew.txt

# View Agent 2's output
echo "=== AGENT 2 OUTPUT (Hebrew) ==="
cat outputs/manual_test/agent2_hebrew.txt
```

### Step 4: Execute Agent 3 Manually

```bash
# Read Agent 2's output (Hebrew)
HEBREW_TEXT=$(cat outputs/manual_test/agent2_hebrew.txt)

# Read Agent 3's skill
AGENT3_SKILL=$(cat agent3_skill.txt)

# For Gemini:
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${GOOGLE_API_KEY}" \
  -H "Content-Type: application/json" \
  -d "{
    \"contents\": [{
      \"parts\": [{
        \"text\": \"${AGENT3_SKILL}\\n\\nUser input:\\n${HEBREW_TEXT}\"
      }]
    }],
    \"generationConfig\": {
      \"temperature\": 0.3,
      \"maxOutputTokens\": 500
    }
  }" | jq -r '.candidates[0].content.parts[0].text' > outputs/manual_test/agent3_english.txt

# View Agent 3's output
echo "=== AGENT 3 OUTPUT (Final English) ==="
cat outputs/manual_test/agent3_english.txt
```

### Step 5: Compare Results

```bash
echo "================================"
echo "COMPARISON"
echo "================================"
echo "Original Input (noisy):"
echo "The artifical systm works eficiently"
echo ""
echo "Agent 1 (French):"
cat outputs/manual_test/agent1_french.txt
echo ""
echo "Agent 2 (Hebrew):"
cat outputs/manual_test/agent2_hebrew.txt
echo ""
echo "Agent 3 (Final English):"
cat outputs/manual_test/agent3_english.txt
echo ""
echo "================================"
```

---

## 📍 METHOD 3: Full Experiment (All Noise Levels)

This runs all 3 agents through 6 different noise levels (0% to 50%).

### Step 1: Choose API and Install Dependencies

**For Gemini:**
```bash
export GOOGLE_API_KEY="your-key"
pip install -r requirements_gemini.txt
chmod +x run_full_experiment_gemini.sh
```

**For OpenAI:**
```bash
export OPENAI_API_KEY="your-key"
pip install -r requirements.txt
chmod +x run_full_experiment.sh
```

### Step 2: Run Full Experiment

**For Gemini:**
```bash
./run_full_experiment_gemini.sh
```

**For OpenAI:**
```bash
./run_full_experiment.sh
```

**What happens:**
- Runs 6 experiments (noise levels: 0%, 10%, 20%, 30%, 40%, 50%)
- Each experiment runs all 3 agents in sequence
- Total: 18 agent executions (6 × 3)
- Takes 2-3 minutes
- Creates 6 output directories

### Step 3: Analyze Results

**For Gemini:**
```bash
python3 analyze_results_gemini.py
```

**For OpenAI:**
```bash
python3 analyze_results.py
```

### Step 4: View Graph

```bash
open semantic_drift_analysis.png
```

**The graph shows:**
- X-axis: Noise percentage (0% → 50%)
- Y-axis: Semantic distance (how much meaning drifted)
- Lower distance = Better performance!

---

## 📂 Understanding the Output Structure

After running agents, you get:

```
outputs/
├── noise_0/              # 0% noise (clean text)
│   ├── agent1_french.txt     # Agent 1's output
│   ├── agent2_hebrew.txt     # Agent 2's output
│   └── agent3_english.txt    # Agent 3's output (final)
├── noise_10/             # 10% noise (2 misspelled words)
│   ├── agent1_french.txt
│   ├── agent2_hebrew.txt
│   └── agent3_english.txt
├── noise_20/             # 20% noise (3 misspelled words)
├── noise_30/             # 30% noise (5 misspelled words)
├── noise_40/             # 40% noise (6 misspelled words)
└── noise_50/             # 50% noise (8 misspelled words)
```

---

## 🧪 Quick Test Examples

### Example 1: Test with Clean Text (0% noise)
```bash
./run_agent_chain_gemini.sh 0 "The artificial intelligence system can efficiently process natural language and understand complex semantic relationships within textual data."
```

### Example 2: Test with Light Noise (10%)
```bash
./run_agent_chain_gemini.sh 10 "The artifical intelligence systm can efficiently process natural language and understand complex semantic relationships within textual data."
```

### Example 3: Test with Heavy Noise (50%)
```bash
./run_agent_chain_gemini.sh 50 "The artifical inteligence systm can eficiently proces naturel langauge and understnd complx semantic relatioships withn textul data."
```

---

## 🔍 How Agents Are Implemented (Technical)

### Agent Structure

Each agent consists of:

1. **Skill File** (e.g., `agent1_skill.txt`)
   - Plain text file
   - Contains the system prompt
   - Defines agent's role and instructions

2. **API Call** (in shell script)
   - Reads the skill file
   - Constructs JSON payload
   - Sends HTTP POST request to API
   - Parses JSON response

3. **Output**
   - Saves result to text file
   - Passes to next agent

### Data Flow

```
agent1_skill.txt → [API Call] → agent1_french.txt
                                        ↓
agent2_skill.txt → [API Call] → agent2_hebrew.txt
                                        ↓
agent3_skill.txt → [API Call] → agent3_english.txt
```

### Shell Script Structure

```bash
# 1. Read skill file
AGENT1_SKILL=$(cat agent1_skill.txt)

# 2. Get input
INPUT_TEXT="The artifical text"

# 3. Create JSON payload
PAYLOAD='{"contents": [{"parts": [{"text": "..."}]}]}'

# 4. Call API
RESPONSE=$(curl -X POST "api-endpoint" -d "$PAYLOAD")

# 5. Parse response
OUTPUT=$(echo "$RESPONSE" | jq -r '.path.to.text')

# 6. Save output
echo "$OUTPUT" > agent1_french.txt

# 7. Pass to next agent (Agent 2 uses this output)
```

---

## ✅ Verification Checklist

Before executing agents:

- [ ] API key is set (`echo $GOOGLE_API_KEY` or `echo $OPENAI_API_KEY`)
- [ ] Dependencies installed (`pip install -r requirements_gemini.txt`)
- [ ] Scripts are executable (`chmod +x run_*.sh`)
- [ ] `jq` is installed (`jq --version`)
- [ ] In correct directory

---

## 🎯 Quick Reference Commands

### Single Execution (Gemini)
```bash
export GOOGLE_API_KEY="your-key"
./run_agent_chain_gemini.sh 30 "Your text with som erors here"
```

### Full Experiment (Gemini)
```bash
export GOOGLE_API_KEY="your-key"
./run_full_experiment_gemini.sh
python3 analyze_results_gemini.py
open semantic_drift_analysis.png
```

### View Results
```bash
# List all outputs
ls -R outputs/

# View specific agent output
cat outputs/noise_30/agent1_french.txt
cat outputs/noise_30/agent2_hebrew.txt
cat outputs/noise_30/agent3_english.txt
```

---

## 🎓 What You're Testing

**Research Question**: How well do LLMs preserve meaning when text has spelling errors?

**Method**:
1. Start with noisy English (spelling errors)
2. Agent 1 fixes it implicitly by translating to French
3. Agent 2 translates French to Hebrew
4. Agent 3 translates Hebrew back to English
5. Compare final English to original clean version
6. Measure semantic drift using vector embeddings

**Expected Result**:
- **Low noise** (0-20%): Minimal drift, agents preserve meaning
- **Medium noise** (30-40%): Slight drift, still good
- **High noise** (50%): More drift, but still recovers well

This tests the **attention mechanism** in LLMs!

---

## 🎉 Summary

**The 3 Agents:**
1. 🤖 **Agent 1**: Fixes noisy English → Outputs French
2. 🤖 **Agent 2**: Takes French → Outputs Hebrew  
3. 🤖 **Agent 3**: Takes Hebrew → Outputs English

**How to Execute:**
- **Easiest**: `./run_full_experiment_gemini.sh`
- **Single Test**: `./run_agent_chain_gemini.sh 30 "your text"`
- **Manual**: Use `curl` commands shown above

**Files Created:**
- `outputs/noise_X/agent1_french.txt`
- `outputs/noise_X/agent2_hebrew.txt`
- `outputs/noise_X/agent3_english.txt`

---

**Ready to run?** Start with:

```bash
export GOOGLE_API_KEY="your-key"
./run_agent_chain_gemini.sh 30 "The artifical systm works eficiently"
```

**Good luck! 🚀✨**

