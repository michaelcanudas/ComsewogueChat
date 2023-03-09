from .utils import search_db


def search(context):
    results = search_db(context, 5, 6)
    date_results = [r[1] for r in results]

    return date_results
