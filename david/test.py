from formatter.request import format_request
from formatter.response import format_responses
from formatter.error import format_error
from responder.answer import answer_questions


def main():
    span = False
    try:
        request = {"question": input(), "past_requests": [], "spanish": True}

        questions, past_questions, span = format_request(request)

        answers = answer_questions(questions, past_questions)

        response = format_responses(answers, span)

        return response
    except Exception as e:
        return format_error(e, span)

print(main())
