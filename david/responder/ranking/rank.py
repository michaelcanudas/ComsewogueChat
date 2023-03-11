from .modules import proximity


def rank(answers, queries, context):
    all_answers = []
    for answer in answers:
        all_answers.extend(answer)

    scores = []
    for answer in all_answers:
        scores.append([answer, [] * len(queries)])

    # every answer option is given a score in each category of query

    # every answer is given multiple scores, one for each
    # answers will be [
    #       [query answer, query answer],
    #       [query answer, query answer, query answer]
    # ]

    # queries will be [
    #       query,
    #       query
    # ]

    # context will be [
    #       context,
    #       context,
    #       context
    # ]

    final_answers = []
    final_context = []

    for answer in answers:
        final_answers.append(answer[0]["query"])
        final_context.append(answer[0]["entry"][0])

    # return [final_answers, queries, context]
    return [final_answers, queries, final_context]
