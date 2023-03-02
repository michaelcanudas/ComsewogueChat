import re
import os
import constants
from abilities import date

pastQueries = []
pastContexts = []

def parse_request(request):
    request = re.sub(r'[^a-zA-Z ]', '', request.lower())
    words = request.split()

    return words


def clean_tokens(tokens):
    queries = filter(lambda w: w not in constants.PUNCTUATION, tokens)
    queries = filter(lambda w: w not in constants.QUERY_STOPWORDS, queries)
    queries = list(queries)

    context = filter(lambda w: w not in constants.PUNCTUATION, tokens)
    context = filter(lambda w: w not in constants.CONTEXT_STOPWORDS, context)
    # check for subjects, noun phrases, verbs, adjectives
    # remove terms from queries (after run through next step)
    context = list(context)

    pastContexts.append(context)

    if not context:
        for i in range(len(pastContexts)-2, -1, -1):
            if pastContexts[i]:
                context = pastContexts[i]
                break

    return queries, context


def classify_queries(queries):
    term_map = {}

    for filename in os.listdir('terms'):
        with open(os.path.join('terms', filename), 'r') as f:
            words = f.read().split()

            for word in words:
                if word in term_map:
                    term_map[word].append(os.path.splitext(filename)[0])
                else:
                    term_map[word] = [os.path.splitext(filename)[0]]

    results_set = set()

    for query in queries:
        if query in term_map:
            results_set.update(term_map[query])

    results = list(results_set)

    pastQueries.append(results)

    if not results:
        for i in range(len(pastQueries)-2, -1, -1):
            if pastQueries[i]:
                results = pastQueries[i]
                break

    return results


# Compute answers
# # From question essence, important phrases, and contextual words, search database in all parts
def search(queries, context):
    answers = []

    # DONT THROW ERROR WHEN COMPUTER IS CONFUSE #
    handlers = {
        "date": date.search,
        "time": lambda c: []
    }

    for query in queries:
        results = handlers[query](context)

        answers.extend(results)

    return answers


def answer(request):
    tokens = parse_request(request)

    (queries, context) = clean_tokens(tokens)

    queries = classify_queries(queries)

    # answers = search(queries, context)

    return queries, context


# add categorization questions (for example: "is tomorrow a snow day", "is tomorrow a b-day")
# all terms should also be context stopwords
