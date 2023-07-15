from flask import Flask, request, abort
import ngrok

app = Flask(__name__)

@app.route("/")
def home():
    return "<p></p>"


@app.route("/webhook", methods=['GET'])
def strava_webhook():
    if request.args.get("hub.verify_token") == "STRAVA":
        return {"hub.challenge": request.args.get("hub.challenge")}
    else:
        return abort(401, description="Could not verify token from Strava API: ")


@app.route("/webhook", methods=['POST'])
def strava_event_listener():
    return {}