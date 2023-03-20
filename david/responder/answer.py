import re
import os
from exceptions.types import *
from .ranking.rank import rank
from .constants import *
from .utils import search_db
from autocorrect import Speller
spell = Speller()


def parse_request(request):
    request = request.replace("-", " ")
    request = request.replace("JV", "Junior Varsity")
    request = re.sub(r'[^a-zA-Z0-9 ]', '', request.lower())
    words = request.split()

    return words


def clean_tokens(tokens):
    queries = filter(lambda w: w not in PUNCTUATION, tokens)

    context = filter(lambda w: w not in PUNCTUATION, tokens)
    context = filter(lambda w: w not in STOPWORDS, context)
    context = filter(lambda w: w not in classify_queries(queries)[0], context)

    return list(queries), list(context)


def classify_queries(queries):
    term_map = {}

    for filename in os.listdir("./responder/terms"):
        with open(os.path.join("./responder/terms", filename), "r") as f:
            words = f.read().split()

            for word in words:
                if word in term_map:
                    term_map[word].append(os.path.splitext(filename)[0])
                else:
                    term_map[word] = [os.path.splitext(filename)[0]]

    results = set()
    indexes = []
    for query in queries:
        i = 0
        if query in term_map:
            indexes.append(i)
            results.update(term_map[query])
        i += 1

    return list(results), indexes


def search(context):
    return search_db(context, 5, 6)


def answer_question(question, past_questions=[]):
    raw_tokens = parse_request(question)
    corrected_tokens = parse_request(spell(question))

    if len(raw_tokens) != len(corrected_tokens):
        raw_tokens = corrected_tokens

    _, context = clean_tokens(raw_tokens)

    queries, _ = clean_tokens(corrected_tokens)
    queries, indexes = classify_queries(queries)

    if queries:
        for i in indexes:
            if raw_tokens[i] != corrected_tokens[i] and raw_tokens[i] in context:
                context.remove(raw_tokens[i])

    i = len(past_questions) - 1
    while i >= 0 and (not context or not queries):
        raw_past_tokens = parse_request(past_questions[i])
        corrected_past_tokens = parse_request(spell(past_questions[i]))

        if not queries:
            queries, _ = clean_tokens(corrected_past_tokens)
            queries = classify_queries(queries)[0]

        if not context:
            _, context = clean_tokens(raw_past_tokens)

        i -= 1

    if not queries and not context:
        raise NoQueryAndContextException()

    if not queries:
        raise NoQueryException(context)

    if not context:
        raise NoContextException(queries)

    try:
        answers, context = search(context)
    except:
        raise NoResultsException(queries, context)

    if not answers:
        raise NoResultsException(queries, context)

    answer = rank(answers, queries, context)

    return answer, queries, context


def answer_questions(questions, past_questions=[]):
    if not questions:
        raise NoQueryAndContextException()

    final_answers = []

    for question in questions:
        answer, queries, context = answer_question(question, past_questions)

        past_questions.append(question)
        final_answers.append(answer)

    return final_answers
