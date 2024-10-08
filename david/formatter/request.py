import re
from googletrans import Translator
from unidecode import unidecode
from exceptions.types import *


def translate(text, target_language):
    translator = Translator()
    translation = None

    if target_language == "english":
        translation = translator.translate(text, dest="en")
    elif target_language == "spanish":
        translation = translator.translate(text, dest="es")

    return translation.text


def format_request(request):
    try:
        question = request["question"]
        span = bool(request["spanish"])
        past_questions = request["past_requests"]
    except Exception:
        raise InvalidRequestException()

    if span:
        question = unidecode(question)
        question = translate(str(question), "english")

    pattern = r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s"
    questions = re.split(pattern, question)

    past_formatted_questions = []
    for i, q in enumerate(past_questions):
        past_formatted_questions.extend(re.split(pattern, q))


    return questions, past_formatted_questions, span
