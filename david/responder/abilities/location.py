from .utils import search_db


def search(context):
    results = search_db(context, 5, 6)

    temp_results = [r[3] for r in results]

    return [temp_results[0]]