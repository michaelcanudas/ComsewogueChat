import re
import os
import constants
from abilities import date, time
from formatoutput import format_output


def parse_request(request):
    request = re.sub(r'[^a-zA-Z ]', '', request.lower())
    words = request.split()

    return words


def clean_tokens(tokens, past_context=None):
    queries = filter(lambda w: w not in constants.PUNCTUATION, tokens)
    queries = list(queries)

    context = filter(lambda w: w not in constants.PUNCTUATION, tokens)
    context = filter(lambda w: w not in constants.CONTEXT_STOPWORDS, context)
    context = filter(lambda w: w not in classify_queries(queries)[0], context)
    context = list(context)

    if not past_context:
        past_context = [context]
    else:
        past_context.append(context)

    if not context:
        for i in range(len(past_context) - 2, -1, -1):
            if past_context[i]:
                context = past_context[i]
                break

    return queries, context, past_context


def classify_queries(queries, past_queries=None):
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

    if not past_queries:
        past_queries = [results]
    else:
        past_queries.append(results)

    if not results:
        for i in range(len(past_queries) - 2, -1, -1):
            if past_queries[i]:
                results = past_queries[i]
                break

    return results, past_queries


def search(queries, context):
    answers = []

    handlers = {
        "date": date.search,
        "time": time.search
    }

    for query in queries:
        results = handlers[query](context)

        answers.extend(results)

    return answers


def answer(request, past_queries=None, past_contexts=None):
    tokens = parse_request(request)

    queries, context, past_contexts = clean_tokens(tokens, past_contexts)

    queries, past_queries = classify_queries(queries, past_queries)

    results = search(queries, context)

    return format_output(queries, context, results), past_queries, past_contexts

# add categorization questions (for example: "is tomorrow a snow day", "is tomorrow a b-day")
