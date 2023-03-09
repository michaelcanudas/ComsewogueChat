from .utils import search_db


def search(context):
    results = search_db(context, 5, 6)
    title_results = [r[0] for r in results]

    return title_results
