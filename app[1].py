from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# ── Config ──────────────────────────────────────
TELEGRAM_TOKEN   = os.environ.get("TELEGRAM_TOKEN", "YOUR_BOT_TOKEN_HERE")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID", "YOUR_CHAT_ID_HERE")
# ────────────────────────────────────────────────

def send_telegram(message: str):
    url  = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "HTML"}
    requests.post(url, data=data)

@app.route("/alert", methods=["POST"])
def alert():
    try:
        payload = request.get_json(force=True) or {}
        symbol  = payload.get("symbol", "UNKNOWN")
        price   = payload.get("price",  "—")
        time_   = payload.get("time",   "—")

        msg = (
            f"🟢 <b>SMC BUY SIGNAL</b>\n"
            f"━━━━━━━━━━━━━━━\n"
            f"📌 Stock  : <b>{symbol}</b>\n"
            f"💰 Price  : <b>₹{price}</b>\n"
            f"🕐 Time   : {time_}\n"
            f"━━━━━━━━━━━━━━━\n"
            f"✅ TL Break + OB + 4H Clean"
        )
        send_telegram(msg)
        return jsonify({"status": "ok"}), 200

    except Exception as e:
        return jsonify({"status": "error", "msg": str(e)}), 500

@app.route("/")
def home():
    return "SMC Alert Bot Running ✅", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
