import math
import datetime
from .constants import *


def rank(ranks, queries, context):
    max_difference = None

    for entry in ranks:
        date = datetime.datetime.strptime(entry["answer"]["entry"][1], "%B %d, %Y").date()
        difference = math.fabs((date - datetime.datetime.today().date()).total_seconds())

        if not max_difference or difference > max_difference:
            max_difference = difference
    
    for entry in ranks:
        date = datetime.datetime.strptime(entry["answer"]["entry"][1], "%B %d, %Y").date()
        difference = math.fabs((date - datetime.datetime.today().date()).total_seconds())
        score = 1 - (difference / max_difference)

        entry["score"] += score * PROXIMITY_WEIGHT

    #closest_difference = None
    #closest_entry = None

    #for entry in ranks:
    #    date = datetime.datetime.strptime(entry["answer"]["entry"][1], "%B %d, %Y").date()
    #    difference = math.fabs((date - datetime.datetime.today().date()).total_seconds())
    #
    #    if not closest_difference or difference < closest_difference:
    #        closest_difference = difference
    #        closest_entry = entry
    #
    #if closest_entry:
    #    closest_entry["score"] += PROXIMITY_WEIGHT
