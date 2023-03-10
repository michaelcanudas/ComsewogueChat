from .utils import search_db


def search(context):
    results = search_db(context, 5, 6)
    title_results = [{
        "query": r["data"][0],
        "entry": r["data"],
        "keywords": r["keywords"]
    } for r in results]

    return title_results
