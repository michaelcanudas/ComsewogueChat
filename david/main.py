import constants
import re
import os

pastQueries = []
pastContexts = []

def parse_request(request):
    #code to check if reuqest is multiple sentences

    #if re.search(r'[.?!](?=\s*[a-zA-Z])', request):
        #raise ValueError('Input must be only one sentence or phrase.')

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


def compute_inputs(inputs):
    # compute neural network from inputs to outputs
    # where outputs are question types (who, when, where, etc)

    # return outputs
    return []


# Compute answers
# # From question essence, important phrases, and contextual words, search database in all parts
def search(outputs, context):
    answers = []

    search_locations = {
        constants.NET_OUT_WHEN: { Calandar: True, Site: False }
    }

    for output in outputs:
        location = search_locations[output]

        if location.Site:
            # database.search(___,0)
            # based on outputs, filter response
            pass

        if location.Calandar:
            # database.search(___,1)
            # based on outputs, filter response
            pass

    # rank by number of keywords in each result

    return answers


def answer(request):
    tokens = parse_request(request)

    (queries, context) = clean_tokens(tokens)

    inputs = classify_queries(queries)

    #outputs = compute_inputs(inputs)

    #answers = search(outputs, context)

    return inputs, context