from abilities import utils


def search(context):
    results = utils.search(context, 5)
    dates = map(lambda r: r.split(",")[1], results)

    return dates
