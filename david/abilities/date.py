from abilities import utils


def search(context):
    results = utils.search(context, 5, 6)

    temp_results = [r[1] for r in results]

    return [temp_results[0]]