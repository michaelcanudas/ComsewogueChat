from flask import Flask, request
from inputformat import format

app = Flask(__name__)

@app.route("/", methods=["POST"])
def main():
    try:
        req = request.get_json()["question"]
        res = format(req)
        return res
    except Exception as e:
        return e
