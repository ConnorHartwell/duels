from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():

    return "<p>HEY WORLD</p>"