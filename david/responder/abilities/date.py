from .utils import search_db


def search(context):
    results = search_db(context, 5, 6)
    date_results = [{
        "query": r["data"][1],
        "entry": r["data"],
        "keywords": r["keywords"]
    } for r in results]

    return date_results
