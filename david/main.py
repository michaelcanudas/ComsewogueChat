from flask import Flask, request
from flask_cors import CORS
from inputformat import format
from importformat import inputformat

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
def main():
    try:
        req = request.get_json()["question"]
        span = bool(request.get_json()["spanish"])
        res = inputformat.format(req, span)
        return res
    except Exception as e:
        return str(e)
