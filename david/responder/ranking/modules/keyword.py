import datetime
from exceptions.types import *
from .constants import *


def rank(ranks, queries, context):
    school_context = list(set(context) & set(SCHOOL_KEYWORDS))
    gender_context = list(set(context) & set(GENDER_KEYWORDS))
    position_context = list(set(context) & set(POSITION_KEYWORDS))

    for word in school_context:
        rank_school(ranks, queries, context, word)
    for word in gender_context:
        rank_gender(ranks, queries, context, word)
    for word in position_context:
        rank_position(ranks, queries, context, word)


def rank_school(ranks, queries, context, word):
    terms = []

    match word:
        case "high" | "highschool":
            terms.extend(["varsity", "junior"])
        case "middle" | "middleschool":
            terms.append("middle")
        case _:
            terms.append(word)

    for entry in ranks:
        first = entry["answer"]["entry"][0].lower().split()[0]

        if first in terms:
            entry["score"] += KEYWORD_WEIGHT
        else:
            ranks.remove(entry)

    if len(ranks) == 0:
        raise NoResultsException(queries, context)


def rank_gender(ranks, queries, context, word):
    for entry in ranks:
        words = entry["answer"]["entry"][0].lower().split()
        if word in words:
            entry["score"] += KEYWORD_WEIGHT
        else:
            ranks.remove(entry)

    if len(ranks) == 0:
        raise NoResultsException(queries, context)


def rank_position(ranks, queries, context, word):
    if word == "next":
        condition = (lambda date, best:
                        True if date >= datetime.datetime.today().date() and ((not best) or date < best)
                        else False)
    else:
        condition = (lambda date, best:
                        True if date <= datetime.datetime.today().date() and ((not best) or date > best)
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
    else:
        raise NoResultsException(queries, context)
