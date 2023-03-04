def format_output(queries, context, answers):
    if len(queries) == 0 and len(context) == 0:
        return "I'm sorry, I don't understand the question."
    if len(queries) == 0:
        return "I'm not sure what you want to know about the " + " ".join(context) + ". Maybe try reformatting your question to include a question word?"

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
        return "What do you want to know the " + queries_str + " of? Maybe try reformatting your question to include some context?"

    answers_str = ""
    if len(answers) > 1:
        answers_str = " and ".join([", ".join(format_answers[:-1]), format_answers[-1]])

    response = "The " + queries_str + " of the " + " ".join(context) + " is " + answers_str + "."
    return response.strip()

