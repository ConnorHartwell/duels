from flask import Flask, request, abort

app = Flask(__name__)
verify_token = "qYdS0Jhjf4LmCmdso5b0d0rRw2jJp6xu"

@app.route("/")
def home():
    return "<p></p>"


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
    # read access code from URL (unsure if needed)
    # check scope has either activity:read OR activity:read_all
    return "<p>You have successfully logged in!</p>"
