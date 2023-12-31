from flask import Flask, request, abort
import requests
import os

app = Flask(__name__)
client_id = os.environ['CLIENT_ID']
client_secret = os.environ['CLIENT_SECRET']
verify_token = "qYdS0Jhjf4LmCmdso5b0d0rRw2jJp6xu"

@app.route("/")
def home():
    return "<p>hello!</p>"


@app.route("/webhook", methods=['GET', 'POST'])
def strava_webhook():
    if(request.method == 'POST'):
        print(request.get_json())
        return ""

    if request.args.get("hub.verify_token") == verify_token:
        return {"hub.challenge": request.args.get("hub.challenge")}
    else:
        return abort(401, description="Could not verify token from Strava API: ")


@app.route("/auth", methods=['GET'])
def auth_user():
    access_code = request.args.get("code")
    if request.args.get("code") != "":
        uri = "https://www.strava.com/oauth/token?client_id={}&code={}&grant_type=authorization_code"\
                    .format(client_id, access_code)
        payload = {"client_secret": client_secret}
        result = requests.post(uri, data=payload)
        if result.status_code == 200:
            return "<p>You have successfully logged in!</p>"
        else:
            print("Request to {} failed with success code {}".format(uri, result.status_code))
    return "<p>Something messed up. Please try again.</p>"
