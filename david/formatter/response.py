from .constants import NO_QC_RESPONSES_1, NO_QC_RESPONSES_2, NO_Q_RESPONSES_1, NO_Q_RESPONSES_2, NO_C_RESPONSES_1a, NO_C_RESPONSES_1b, NO_C_RESPONSES_2
from formatter.request import translate
from unidecode import unidecode
import random


def format_response(queries, context, answers):
    if len(queries) == 0 and len(context) == 0:
        return NO_QC_RESPONSES_1[random.randint(0, 4)] + " " + NO_QC_RESPONSES_2[random.randint(0, 4)]
    if len(queries) == 0:
        return NO_Q_RESPONSES_1[random.randint(0, 3)] + " ".join(context) + NO_Q_RESPONSES_2[random.randint(0, 3)]

    if len(answers) > len(queries):
        for i in range(len(queries)):
            queries[i] = queries[i] + 's'

    queries_str = ", ".join(queries)
    format_answers = []
    if len(queries) > 1:
        queries_str = " and ".join([", ".join(queries[:-1]), queries[-1]])
        inc = int(len(answers)/len(queries))
        for i in range(len(queries)):
            for j in range(inc):
                format_answers.append(answers[i + (j * inc)])
    else:
        format_answers = answers

    if len(context) == 0:
        randint = random.randint(0,2)
        return NO_C_RESPONSES_1a[randint] + queries_str + NO_C_RESPONSES_1b[randint] +  NO_C_RESPONSES_2[random.randint(0, 5)]

    if len(answers) > 1:
        answers_str = " and ".join([", ".join(format_answers[:-1]), format_answers[-1]])
    else:
        answers_str = format_answers[0]

    response = "The " + queries_str + " of the " + " ".join(context) + " is " + answers_str + "."

    return response.strip()


def format_responses(answers, span):
    response = ""

    for answer in answers:
        response += " " + format_response(answer[0], answer[1], answer[2])

        if span:
            response = translate(str(response), "spanish")
        response = unidecode(response)
        if response.startswith('?'):
            response = response[1:]
        if ".?" in response:
            response = response.replace(".?", ". ")
        if "!!" in response:
            response = response.replace("!!", "! ")
        if "??" in response:
            response = response.replace("??", "? ")

    return response
