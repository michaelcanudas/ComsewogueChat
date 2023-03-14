import datetime
from exceptions.types import *
from .constants import *


def rank(ranks, queries, context):
    keywords = {
        "high": rank_school,
        "highschool": rank_school,
        "varsity": rank_school,
        "junior": rank_school,
        "middle": rank_school,
        "middleschool": rank_school,

        "boys": rank_gender,
        "girls": rank_gender,

        "next": rank_next,
        "last": rank_last
    }

    for word in keywords:
        if word in context:
            keywords[word](ranks, queries, context)


def rank_school(ranks, queries, context):
    keywords = None

    if "middle" in context or "middleschool" in context:
        keywords = ["middle"]
    elif "high" in context or "highschool" in context:
        keywords = ["varsity", "junior"]
    elif "varsity" in context:
        keywords = ["varsity"]
    elif "junior" in context:
        keywords = ["junior"]
    else:
        return

    for entry in ranks:
        first = entry["answer"]["entry"][0].lower().split()[0]
        if first in keywords:
            entry["score"] += SCHOOL_WEIGHT
        else:
            ranks.remove(entry)

    if len(ranks) == 0:
        raise NoResultsException(queries, context)


def rank_gender(ranks, queries, context):
    keyword = None

    if "boys" in context:
        keyword = "boys"
    elif "girls" in context:
        keyword = "girls"
    else:
        return

    for entry in ranks:
        words = entry["answer"]["entry"][0].lower().split()
        if keyword in words:
            entry["score"] += SCHOOL_WEIGHT
        else:
            ranks.remove(entry)

    if len(ranks) == 0:
        raise NoResultsException(queries, context)


def rank_next(ranks, queries, context):
    closest_date = None
    closest_entry = None

    for entry in ranks:
        date = datetime.datetime.strptime(entry["answer"]["entry"][1], "%B %d, %Y").date()
        if date >= datetime.datetime.today().date() and (not closest_date or date < closest_date):
            closest_date = date
            closest_entry = entry

    if closest_date:
        closest_entry["score"] += NEXT_WEIGHT
    else:
        raise NoResultsException(queries, context)


def rank_last(ranks, queries, context):
    latest_date = None
    latest_entry = None

    for entry in ranks:
        date = datetime.datetime.strptime(entry["answer"]["entry"][1], "%B %d, %Y").date()
        if date <= datetime.datetime.today().date() and (not latest_date or date > latest_date):
            latest_date = date
            latest_entry = entry

    if latest_date:
        latest_entry["score"] += LAST_WEIGHT
    else:
        raise NoResultsException(queries, context)
