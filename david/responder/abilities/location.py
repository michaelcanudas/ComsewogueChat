from .utils import search_db


def search(context):
    results = search_db(context, 5, 6)
    location_results = [{
        "query": r["data"][3],
        "entry": r["data"],
        "keywords": r["keywords"]
    } for r in results]

    return location_results
