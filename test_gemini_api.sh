#!/bin/bash

# Quick test script to verify Gemini API connection

echo "Testing Gemini API connection..."
echo ""

if [ -z "$GOOGLE_API_KEY" ]; then
    echo "❌ Error: GOOGLE_API_KEY not set"
    echo "Please run: export GOOGLE_API_KEY='your-key'"
    exit 1
fi

echo "✓ API key is set"
echo ""

echo "Testing with gemini-2.0-flash model..."
echo ""

RESPONSE=$(curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=${GOOGLE_API_KEY}" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [{
        "text": "Say hello in French"
      }]
    }]
  }')

echo "Response:"
echo "$RESPONSE" | jq .

# Check if there's an error
ERROR=$(echo "$RESPONSE" | jq -r '.error.message // empty')

if [ -n "$ERROR" ]; then
    echo ""
    echo "❌ API Error: $ERROR"
    echo ""
    echo "Trying to list available models..."
    curl -s "https://generativelanguage.googleapis.com/v1beta/models?key=${GOOGLE_API_KEY}" | jq -r '.models[] | select(.supportedGenerationMethods[] | contains("generateContent")) | .name'
else
    OUTPUT=$(echo "$RESPONSE" | jq -r '.candidates[0].content.parts[0].text // empty')
    if [ -n "$OUTPUT" ]; then
        echo ""
        echo "✅ Success! API is working!"
        echo "Output: $OUTPUT"
    fi
fi

