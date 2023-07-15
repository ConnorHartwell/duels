from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>HEY WORLD</p>"

@app.route("/webhook/strava", methods=['POST'])
def strava_webhook():
