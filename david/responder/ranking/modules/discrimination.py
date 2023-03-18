from .constants import *
import datetime
from exceptions.types import *

def rank(ranks, queries, context):
    school_context = list(set(context) & set(SCHOOL_KEYWORDS))
    gender_context = list(set(context) & set(GENDER_KEYWORDS))
    position_context = list(set(context) & set(POSITION_KEYWORDS))

    if len(school_context) == 0:
        for entry in ranks:
            first = entry["answer"]["entry"][0].lower().split()[0]

            if first == "varsity":
                entry["score"] += DISCRIMINATION_WEIGHT * 2
            if first == "junior":
                entry["score"] += DISCRIMINATION_WEIGHT

    if len(gender_context) == 0:
        for entry in ranks:
            words = entry["answer"]["entry"][0].lower().split()

            if "boys" in words:
                entry["score"] += DISCRIMINATION_WEIGHT

    if len(position_context) == 0:
        condition = (lambda date, best:
                        True if date >= datetime.datetime.today().date() and ((not best) or date < best)
                        else False)

        best_date = None
        best_entry = None

        for entry in ranks:
            date = datetime.datetime.strptime(entry["answer"]["entry"][1], "%B %d, %Y").date()

            if condition(date, best_date):
                best_date = date
                best_entry = entry

        if best_date:
            best_entry["score"] += KEYWORD_WEIGHT

