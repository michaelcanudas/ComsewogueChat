def rank(answers, queries, context):
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

    for answer in answers:
        final_answers.append(answer[0])

    return [final_answers, queries, context]