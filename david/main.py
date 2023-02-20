import constants


def parse_request(request):
    # precondition: only one sentence or phrase

    # split request by words

    # return words
    return []


def clean_tokens(tokens):
    queries = []
    context = []
  
    queries = filter(lambda w: w not in constants.PUNCTUATION, tokens)
    queries = filter(lambda w: w not in constants.QUERY_STOPWORDS, queries)
    queries = list(queries)

    context = filter(lambda w: w not in constants.PUNCTUATION, tokens)
    context = filter(lambda w: w not in constants.CONTEXT_STOPWORDS, context)
    # check for subjects, noun phrases, verbs, adjectives
    # remove terms from queries (after run through next step)
    context = list(context)

    return queries, context


def classify_queries(queries):
    # for every query, check similarity to every input node
    # if strong enough, convert queries

    # return inputs
    return []


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

    outputs = compute_inputs(inputs)

    answers = search(outputs, context)

    return answers

search(["when"])