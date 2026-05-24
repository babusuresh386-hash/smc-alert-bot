# SMC Alert Bot — Setup Guide

## Files:
- app.py          → Main Flask server
- requirements.txt→ Python packages
- render.yaml     → Render.com config

## Deploy Steps:

### 1. GitHub
- GitHub.com → New repo → "smc-alert-bot"
- இந்த 3 files upload பண்ணுங்க

### 2. Render.com (Free hosting)
- render.com → Sign up (GitHub account மூலம்)
- "New Web Service" → உங்க GitHub repo select
- Environment Variables set பண்ணுங்க:
    TELEGRAM_TOKEN   = (BotFather-கிட்ட கிடைச்சது)
    TELEGRAM_CHAT_ID = (getUpdates-ல் கிடைச்சது)
- Deploy click → URL கிடைக்கும் (example: https://smc-alert-bot.onrender.com)

### 3. TradingView Alert
- Chart → Alert → Create Alert
- Condition: SMC Buy signal
- Webhook URL: https://smc-alert-bot.onrender.com/alert
- Message:
  {"symbol": "{{ticker}}", "price": "{{close}}", "time": "{{time}}"}

## Done!
Signal வந்தா Telegram-ல் உடனே message வரும் 🎯
