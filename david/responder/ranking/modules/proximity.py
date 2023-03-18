import math
import datetime
from .constants import *


def rank(ranks, queries, context):
    max_difference = None

    for entry in ranks:
        date = datetime.datetime.strptime(entry["answer"]["entry"][1].split("; ")[0], "%B %d, %Y").date()
        difference = math.fabs((date - datetime.datetime.today().date()).total_seconds())

        if not max_difference or difference > max_difference:
            max_difference = difference
    
    for entry in ranks:
        date = datetime.datetime.strptime(entry["answer"]["entry"][1].split("; ")[0], "%B %d, %Y").date()
        difference = math.fabs((date - datetime.datetime.today().date()).total_seconds())
        score = 1 - (difference / max_difference)

        entry["score"] += score * PROXIMITY_WEIGHT
