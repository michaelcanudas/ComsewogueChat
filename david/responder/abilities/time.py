from .utils import search_db


def search(context):
    results = search_db(context, 5, 6)
    time_results = [{
        "query": r["data"][2],
        "entry": r["data"],
        "keywords": r["keywords"]
    } for r in results]

    return time_results
