from flask import Flask, request as req
from flask_cors import CORS
from formatter.request import format_request
from formatter.response import format_responses
from responder.answer import answer_questions


app = Flask(__name__)
CORS(app)


@app.route("/", methods=["POST"])
def main():
    try:
        request = req.get_json()

        questions, past_questions, span = format_request(request)
        #if err:
        #    return format_error(err)

        answers = answer_questions(questions, past_questions)
            # return an error message

        response = format_responses(answers, span)
        #if err:
        #    return format_error(err)

        # res = format(req["question"], bool(req["spanish"]))

        return response
    except Exception as e:
        return "[ERROR] Unhandled Exception: " + str(e)
