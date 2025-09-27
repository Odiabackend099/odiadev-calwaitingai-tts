#!/bin/bash

# CallWaiting.ai TTS Repository Push Script
# This script will help you push your TTS repository to GitHub

echo "🚀 CallWaiting.ai TTS Repository Push Script"
echo "=========================================="

cd /Users/odiadev/Desktop/tts/Odiadev-callwaitingai-tts

echo "📁 Current directory: $(pwd)"
echo "📋 Repository status:"
git status

echo ""
echo "🔐 GitHub Authentication Required"
echo "To push to GitHub, you need to authenticate. Here are your options:"
echo ""
echo "Option 1: Use Personal Access Token"
echo "1. Go to: https://github.com/settings/tokens"
echo "2. Generate new token with 'repo' permissions"
echo "3. Copy the token"
echo "4. Run: git push -u origin main"
echo "   - Username: Odiabackend099"
echo "   - Password: paste your token"
echo ""
echo "Option 2: Use GitHub CLI"
echo "1. Install: brew install gh"
echo "2. Run: gh auth login"
echo "3. Run: git push -u origin main"
echo ""
echo "Option 3: Manual Push"
echo "Run this command and enter your credentials when prompted:"
echo "git push -u origin main"
echo ""

# Show current remote
echo "🌐 Current remote URL:"
git remote -v

echo ""
echo "📦 Files ready to push:"
ls -la

echo ""
echo "✅ Repository is ready! Just authenticate and push."
