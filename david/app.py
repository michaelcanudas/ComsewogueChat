from flask import Flask, request
from flask_cors import CORS
from inputformat import format


app = Flask(__name__)
CORS(app)


@app.route("/", methods=["POST"])
def main():
    try:
        req = request.get_json()["question"]
        span = bool(request.get_json()["spanish"])
        res = format(req, span)
        return res
    except Exception as e:
        return str(e)
