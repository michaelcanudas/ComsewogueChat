from .utils import search_db


def search(context):
    # opponent_result[0].split(":")[1].replace("@", "").replace("Comsewogue Jfk", "").replace("Comsewogue", "").strip()
    results = search_db(context, 5, 6)
    opponent_results = [{
        "query": r["data"][0],
        "entry": r["data"],
        "keywords": r["keywords"]
    } for r in results]

    return opponent_results
