#!/bin/bash

# Agentic Turing Machine - CLI Agent Chain Execution (Google Gemini Version)
# This script runs the 3-agent translation pipeline: English -> French -> Hebrew -> English
# Pure CLI implementation - NO Python for orchestration
# Uses Google Gemini API instead of OpenAI

set -e  # Exit on error

# Configuration
API_KEY="${GOOGLE_API_KEY}"
if [ -z "$API_KEY" ]; then
    echo "Error: GOOGLE_API_KEY environment variable not set"
    echo "Please set it with: export GOOGLE_API_KEY='your-key-here'"
    exit 1
fi

# Gemini API configuration
MODEL="gemini-2.0-flash"  # Using stable Gemini 2.0 Flash model
API_BASE_URL="https://generativelanguage.googleapis.com/v1beta/models"

# Input parameters
NOISE_LEVEL="$1"
INPUT_TEXT="$2"

if [ -z "$NOISE_LEVEL" ] || [ -z "$INPUT_TEXT" ]; then
    echo "Usage: $0 <noise_level> <input_text>"
    echo "Example: $0 0 'The artificial intelligence system...'"
    exit 1
fi

# Create output directory
OUTPUT_DIR="outputs/noise_${NOISE_LEVEL}"
mkdir -p "$OUTPUT_DIR"

echo "========================================"
echo "Running Agent Chain - Noise Level: ${NOISE_LEVEL}%"
echo "Using Google Gemini API"
echo "========================================"

# Read system prompts
AGENT1_PROMPT=$(cat agent1_skill.txt)
AGENT2_PROMPT=$(cat agent2_skill.txt)
AGENT3_PROMPT=$(cat agent3_skill.txt)

# ============================================
# AGENT 1: English (Noisy) -> French
# ============================================
echo ""
echo ">>> Agent 1: Translating English to French..."
echo "Input: $INPUT_TEXT"

# Create JSON payload for Agent 1 (Gemini format)
# Gemini uses "contents" with "parts" structure
AGENT1_PAYLOAD=$(cat <<EOF
{
  "contents": [
    {
      "parts": [
        {
          "text": $(echo "${AGENT1_PROMPT}\n\nUser input:\n${INPUT_TEXT}" | jq -Rs .)
        }
      ]
    }
  ],
  "generationConfig": {
    "temperature": 0.3,
    "maxOutputTokens": 500
  }
}
EOF
)

# Call Agent 1
AGENT1_RESPONSE=$(curl -s -X POST "${API_BASE_URL}/${MODEL}:generateContent?key=${API_KEY}" \
  -H "Content-Type: application/json" \
  -d "$AGENT1_PAYLOAD")

# Extract French output (Gemini response structure)
FRENCH_OUTPUT=$(echo "$AGENT1_RESPONSE" | jq -r '.candidates[0].content.parts[0].text // empty')

if [ -z "$FRENCH_OUTPUT" ]; then
    echo "Error: Agent 1 failed to produce output"
    echo "Response: $AGENT1_RESPONSE"
    exit 1
fi

echo "Output: $FRENCH_OUTPUT"
echo "$FRENCH_OUTPUT" > "$OUTPUT_DIR/agent1_french.txt"

# ============================================
# AGENT 2: French -> Hebrew
# ============================================
echo ""
echo ">>> Agent 2: Translating French to Hebrew..."
echo "Input: $FRENCH_OUTPUT"

# Create JSON payload for Agent 2
AGENT2_PAYLOAD=$(cat <<EOF
{
  "contents": [
    {
      "parts": [
        {
          "text": $(echo "${AGENT2_PROMPT}\n\nUser input:\n${FRENCH_OUTPUT}" | jq -Rs .)
        }
      ]
    }
  ],
  "generationConfig": {
    "temperature": 0.3,
    "maxOutputTokens": 500
  }
}
EOF
)

# Call Agent 2
AGENT2_RESPONSE=$(curl -s -X POST "${API_BASE_URL}/${MODEL}:generateContent?key=${API_KEY}" \
  -H "Content-Type: application/json" \
  -d "$AGENT2_PAYLOAD")

# Extract Hebrew output
HEBREW_OUTPUT=$(echo "$AGENT2_RESPONSE" | jq -r '.candidates[0].content.parts[0].text // empty')

if [ -z "$HEBREW_OUTPUT" ]; then
    echo "Error: Agent 2 failed to produce output"
    echo "Response: $AGENT2_RESPONSE"
    exit 1
fi

echo "Output: $HEBREW_OUTPUT"
echo "$HEBREW_OUTPUT" > "$OUTPUT_DIR/agent2_hebrew.txt"

# ============================================
# AGENT 3: Hebrew -> English
# ============================================
echo ""
echo ">>> Agent 3: Translating Hebrew to English..."
echo "Input: $HEBREW_OUTPUT"

# Create JSON payload for Agent 3
AGENT3_PAYLOAD=$(cat <<EOF
{
  "contents": [
    {
      "parts": [
        {
          "text": $(echo "${AGENT3_PROMPT}\n\nUser input:\n${HEBREW_OUTPUT}" | jq -Rs .)
        }
      ]
    }
  ],
  "generationConfig": {
    "temperature": 0.3,
    "maxOutputTokens": 500
  }
}
EOF
)

# Call Agent 3
AGENT3_RESPONSE=$(curl -s -X POST "${API_BASE_URL}/${MODEL}:generateContent?key=${API_KEY}" \
  -H "Content-Type: application/json" \
  -d "$AGENT3_PAYLOAD")

# Extract final English output
FINAL_ENGLISH=$(echo "$AGENT3_RESPONSE" | jq -r '.candidates[0].content.parts[0].text // empty')

if [ -z "$FINAL_ENGLISH" ]; then
    echo "Error: Agent 3 failed to produce output"
    echo "Response: $AGENT3_RESPONSE"
    exit 1
fi

echo "Output: $FINAL_ENGLISH"
echo "$FINAL_ENGLISH" > "$OUTPUT_DIR/agent3_english.txt"

# ============================================
# SUMMARY
# ============================================
echo ""
echo "========================================"
echo "Agent Chain Complete!"
echo "========================================"
echo "Original Input: $INPUT_TEXT"
echo "French (Agent 1): $FRENCH_OUTPUT"
echo "Hebrew (Agent 2): $HEBREW_OUTPUT"
echo "Final English (Agent 3): $FINAL_ENGLISH"
echo ""
echo "Results saved to: $OUTPUT_DIR/"
echo "========================================"

