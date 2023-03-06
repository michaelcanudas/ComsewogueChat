from .request import translate
from unidecode import unidecode


def format_response(queries, context, answers):

    if len(answers) > len(queries):
        for i in range(len(queries)):
            queries[i] += 's'

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
