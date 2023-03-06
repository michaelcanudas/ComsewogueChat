import re
# import answer

from googletrans import Translator
from unidecode import unidecode
from autocorrect import Speller
spell = Speller()


def translate(text, target_language):
    translator = Translator()
    translation = None

    if target_language == "english":
        translation = translator.translate(text, dest="en")
    elif target_language == "spanish":
        translation = translator.translate(text, dest="es")

    return translation.text


def format_request(request):
    question = request["question"]
    span = bool(request["spanish"])

    if span:
        question = unidecode(question)
        question = translate(str(question), "english")

    question = spell(question)

    pattern = r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s"
    questions = re.split(pattern, question)

    past_questions = request["past_requests"]
    past_formatted_questions = []
    for q in past_questions:
        q = spell(q)
        past_formatted_questions.extend(re.split(pattern, q))

    return questions, past_formatted_questions, span