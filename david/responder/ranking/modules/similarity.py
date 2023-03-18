from .constants import *


def rank(ranks, queries, context):
    max_count = -1
    for entry in ranks:
        count = len(entry["answer"]["keywords"])
        if count > max_count:
            max_count = count

    for entry in ranks:
        count = len(entry["answer"]["keywords"])
        score = count / max_count

        entry["score"] += score * SIMILARITY_WEIGHT
