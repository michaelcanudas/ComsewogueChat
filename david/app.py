from flask import Flask, request as req
from flask_cors import CORS
from formatter.request import format_request
from formatter.response import format_responses
from formatter.error import format_error
from responder.answer import answer_questions
import json


app = Flask(__name__)
CORS(app)

@app.route("/", methods=["POST"])
def main():
    span = False
    try:
        request = req.get_json()

        questions, past_questions, span = format_request(request)
        
        answers = answer_questions(questions, past_questions)

        response = format_responses(answers, span)

        return json.dumps({
            "response": response,
            "success": True
        })
    except Exception as e:
        return json.dumps({
            "response": format_error(e, span),
            "success": False
        })

@app.route("/feedback", methods=["POST"])
def feedback():
    try:
        request = req.get_json()

        question = request["question"]
        answer = request["answer"]
        feedback = request["feedback"]

        pass
    except Exception as e:
        return "omg..."