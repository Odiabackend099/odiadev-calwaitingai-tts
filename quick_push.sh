#!/bin/bash

# Quick Push Script for CallWaiting.ai TTS
echo "🚀 Quick Push to GitHub"
echo "====================="

cd /Users/odiadev/Desktop/tts/Odiadev-callwaitingai-tts

echo "📦 Repository ready to push:"
git status

echo ""
echo "🔐 To push, you need a GitHub Personal Access Token:"
echo "1. Go to: https://github.com/settings/tokens"
echo "2. Generate new token with 'repo' access"
echo "3. Copy the token"
echo ""
echo "Then run this command:"
echo "git push -u origin main"
echo ""
echo "When prompted:"
echo "- Username: Odiabackend099"
echo "- Password: [paste your token]"
echo ""
echo "Or use this one-liner with your token:"
echo "git remote set-url origin https://YOUR_TOKEN@github.com/Odiabackend099/odiadev-calwaitingai-tts.git && git push -u origin main"
