from abilities import utils


def search(context):
    results = utils.search(context, 5, 6)

    temp_results = [r[2] for r in results]

    return [temp_results[0]]
