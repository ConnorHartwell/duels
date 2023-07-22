from flask import Flask, request, abort
import requests

app = Flask(__name__)
client_id = 110630
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
        result = requests.get(uri)
        if result.status_code == 200:
            return "<p>You have successfully logged in!</p>"
    # read access code from URL (unsure if needed)
    # check scope has either activity:read OR activity:read_all
    return "<p>Something messed up. Please try again.</p>"
