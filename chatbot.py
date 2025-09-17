import requests
from flask import Flask, request
import qrcode
import openai
import pytz
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "WhatsApp Bot (Python Version) is running ✅"

@app.route("/time")
def get_time():
    tz = pytz.timezone("Africa/Nairobi")
    return f"Current time in Nairobi: {datetime.now(tz).strftime('%Y-%m-%d %H:%M:%S')}"

@app.route("/ai", methods=["POST"])
def ask_ai():
    data = request.json
    prompt = data.get("prompt", "")
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    return {"response": response.choices[0].text.strip()}

if __name__ == "__main__":
    app.run(port=5000)