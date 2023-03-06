from flask import Flask, request as req
from flask_cors import CORS
from formatter.request import format_request
from formatter.response import format_responses
#from formatter.error import format_error
from responder.answer import answer_questions


app = Flask(__name__)
CORS(app)


@app.route("/", methods=["POST"])
def main():
    try:
        request = req.get_json()

        questions, past_questions, span = format_request(request)

        answers = answer_questions(questions, past_questions)

        response = format_responses(answers, span)

        return response
    except Exception as e:
        #return format_error(e)
        return "OMG!"
