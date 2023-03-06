import random
from david.exceptions.types import *
from .constants import *
import random

def format_error(exception):

    if exception is InvalidRequestException:
        return "", 400

    if exception is NoQueryAndContextException:
        return NO_QC_RESPONSES_1[random.randint(0, 4)] + " " + NO_QC_RESPONSES_2[random.randint(0, 4)]

    elif exception is NoQueryException:
        return NO_Q_RESPONSES_1[random.randint(0, 3)] + " ".join(exception.context) + NO_Q_RESPONSES_2[random.randint(0, 3)]

    elif exception is NoContextException:
        randint = random.randint(0,2)
        if len(exception.queries) > 1:
            queries_str = " and ".join([", ".join(exception.queries[:-1]), exception.queries[-1]])
        else:
            queries_str = ", ".join(exception.queries)
        return NO_C_RESPONSES_1a[randint] + queries_str + NO_C_RESPONSES_1b[randint] +  NO_C_RESPONSES_2[random.randint(0, 5)]

    # elif exception is NoResultsException:
        # return "Sorry, I could find any results for the " ... " of " ... ". Maybe try rephrasing your question or "
