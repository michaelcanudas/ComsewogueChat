import re
import os
from .abilities import date, time
from .constants import PUNCTUATION, STOPWORDS


def parse_request(request):
    request = re.sub(r'[^a-zA-Z ]', '', request.lower())
    words = request.split()

    return words


def clean_tokens(tokens):
    queries = filter(lambda w: w not in PUNCTUATION, tokens)

    context = filter(lambda w: w not in PUNCTUATION, tokens)
    context = filter(lambda w: w not in STOPWORDS, context)
    context = filter(lambda w: w not in classify_queries(queries), context)

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
    for query in queries:
        if query in term_map:
            results.update(term_map[query])

    return list(results)


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


def answer_question(question, past_questions=[]):
    tokens = parse_request(question)

    queries, context = clean_tokens(tokens)

    queries = classify_queries(queries)

    i = len(past_questions) - 1
    while i >= 0 and (not context or not queries):
        past_tokens = parse_request(past_questions[i])

        if not context:
            _, context = clean_tokens(past_tokens)

        if not queries:
            queries, _ = clean_tokens(past_tokens)
            queries = classify_queries(queries)

        i -= 1

    answer = search(queries, context)

    return answer, queries, context


def answer_questions(questions, past_questions=[]):
    answers = []

    for question in questions:
        answer, queries, contexts = answer_question(question, past_questions)
        past_questions.append(question)

        answers.append([queries, contexts, answer])

    return answers
