from .utils import search_db


def search(context):
    # opponent_result[0].split(":")[1].replace("@", "").replace("Comsewogue Jfk", "").replace("Comsewogue", "").strip()
    results = search_db(context, 5, 6)
    opponent_results = [r[0] for r in results]

    return opponent_results
