import constants


def parse_request(request):
    # precondition: only one sentence or phrase

    # split request by words

    # return words
    return []


def clean_tokens(tokens):
    # remove punctuation
    # remove stopwords
    # remove manual override words
    # assign to queries

    # remove punctuation
    # check for noun phrases
    # check for verbs/adjectives
    # check for subjects
    # assign to context

    # return (queries, context)
    return [], []


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