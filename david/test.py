from formatter.request import format_request
from formatter.response import format_responses
from formatter.error import format_error
from responder.answer import answer_questions

def main():
    try:
        request = {"question": input(), "past_requests": [], "spanish": False}

        questions, past_questions, span = format_request(request)
            #if err:
            #    return format_error(err)

        answers = answer_questions(questions, past_questions)
            #if err:
            #    return format_error(err)

        response = format_responses(answers, span)
            #if err:
            #    return format_error(err)

            # res = format(req["question"], bool(req["spanish"]))

        return response
    except Exception as e:
        return format_error(e)

print(main())
