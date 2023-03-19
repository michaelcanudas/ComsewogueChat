from formatter.request import format_request
from formatter.response import format_responses
from formatter.error import format_error
from responder.answer import answer_questions
import time


def main():
    span = False
    try:
        request = {"question": input(), "past_requests": [], "spanish": False}

        t0 = time.time()

        try:
            questions, past_questions, span = format_request(request, False)
            answers = answer_questions(questions, past_questions)
        except Exception as e:
            try:
                questions, past_questions, span = format_request(request, True)
                answers = answer_questions(questions, past_questions)
            except:
                raise e

        response = format_responses(answers, span)
        t1 = time.time()

        return "[SUCCESS]", response, t1 - t0
    except Exception as e:
        raise e

test = main()
print(test[0], "[TIME=" + str(test[2]) + "]", test[1])
