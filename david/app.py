from flask import Flask, request
from flask_cors import CORS
from importformat import inputformat


app = Flask(__name__)
CORS(app)


@app.route("/", methods=["POST"])
def main():
    print("STEP 3")
    try:
        req = request.get_json()["question"]
        span = bool(request.get_json()["spanish"])
        res = inputformat.format(req, span)
        return res
    except Exception as e:
        return str(e)
