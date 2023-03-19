from .constants import *
from exceptions.types import *


def rank(ranks, queries, context):
    max_count = -1
    for entry in ranks:
        count = len(entry["answer"]["keywords"])
        if count > max_count:
            max_count = count

    for entry in ranks:
        count = len(entry["answer"]["keywords"])
        score = count / max_count

        if count > len(context)/3.5:
            entry["score"] += score * SIMILARITY_WEIGHT
        else:
            raise NoResultsException(queries, context)

