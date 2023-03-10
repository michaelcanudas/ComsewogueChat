import random
from exceptions.types import *
from .constants import *
import random
from .request import translate
from unidecode import unidecode

def format_error(exception, span):

    if type(exception) == InvalidRequestException:
        error = "", 400

    elif type(exception) == NoQueryAndContextException:
        error = NO_QC_RESPONSES_1[random.randint(0, 4)] + " " + NO_QC_RESPONSES_2[random.randint(0, 4)]

    elif type(exception) == NoQueryException:
        error = NO_Q_RESPONSES_1[random.randint(0, 3)] + " ".join(exception.context) + NO_Q_RESPONSES_2[random.randint(0, 3)]

    elif type(exception) == NoContextException:
        randint = random.randint(0,2)
        if len(exception.queries) > 1:
            queries_str = " and ".join([", ".join(exception.queries[:-1]), exception.queries[-1]])
        else:
            queries_str = ", ".join(exception.queries)
        error = NO_C_RESPONSES_1a[randint] + queries_str + NO_C_RESPONSES_1b[randint] +  NO_C_RESPONSES_2[random.randint(0, 5)]

    elif type(exception) == NoResultsException:
        if len(exception.queries) > 1:
            queries_str = " or ".join([", ".join(exception.queries[:-1]), exception.queries[-1]])
        else:
            queries_str = ", ".join(exception.queries)
        error = NO_R_RESPONSES_1[random.randint(0, 3)] + queries_str + " of " + " ".join(exception.context) + NO_R_RESPONSES_2[random.randint(0, 2)]

    else:
        error = "An unexpected error has occured. Our team has been notified of the issue and is working to resolve it. Please try again later"
        # error = "wat the heck!"

    if not span:
        return error
    else:
        error = translate(str(error), "spanish")
        error = unidecode(error)
        if error.startswith('?'):
            error = error[1:]
        if ".?" in error:
            error = error.replace(".?", ". ")
        if "!!" in error:
            error = error.replace("!!", "! ")
        if "??" in error:
            error = error.replace("??", "? ")
        return error
