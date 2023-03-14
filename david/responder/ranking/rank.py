from .modules import keyword, proximity, similarity


def rank(answers, queries, context):
    ranks = []
    for answer in answers[0]:
        ranks.append({
            "answer": answer,
            "score": 0
        })

    keyword.rank(ranks, queries, context)

    #proximity.rank(ranks, context)

    #similarity.rank(ranks, context)

    max_score = -1
    max_answer = {}
    for entry in ranks:
        if entry["score"] > max_score:
            max_score = entry["score"]
            max_answer = entry["answer"]

    query_answers = []
    for query in queries:
        match query:
            case "date":
                query_answers.append(max_answer["entry"][1])
            case "location":
                query_answers.append(max_answer["entry"][3])
            case "opponent":
                query_answers.append(max_answer["entry"][0].split(":")[1].replace("@", "").replace("Comsewogue Jfk", "").replace("Comsewogue", "").strip())
            case "time":
                query_answers.append(max_answer["entry"][2])
            case "title":
                query_answers.append(max_answer["entry"][0])

    return [query_answers, queries, context]
