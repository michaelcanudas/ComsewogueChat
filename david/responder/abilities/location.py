from .utils import search_db


def search(context):
    results = search_db(context, 5, 6)
    location_results = [r[3] for r in results]

    return location_results
