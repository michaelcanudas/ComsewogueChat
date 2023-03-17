from .constants import *


def rank(ranks, queries, context):
    school_context = list(set(context) & set(SCHOOL_KEYWORDS))
    gender_context = list(set(context) & set(GENDER_KEYWORDS))

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
