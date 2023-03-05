import re
import answer

from googletrans import Translator
from unidecode import unidecode

def translate(text, target_language):
    translator = Translator()
    if target_language == "english":
        translation = translator.translate(text, dest="en")
        return translation.text
    elif target_language == "spanish":
        translation = translator.translate(text, dest="es")
        return translation.text

pattern = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s'

def format(input, span):
    if span:
        input = unidecode(input)
        input = translate(str(input), "english")

    pastQueries = []
    pastContexts = []

    sentences = re.split(pattern, input)

    answers = []
    for sentence in sentences:
        output, pastQueries, pastContexts = answer.answer(sentence, pastQueries, pastContexts)
        if span:
            output = translate(str(output), "spanish")
            output = unidecode(output)
            if output.startswith('?'):
                output = output[1:]
            if ".?" in output:
                output = output.replace(".?", ". ")
            if "!!" in output:
                output = output.replace("!!", "! ")
            if "??" in output:
                output = output.replace("??", "? ")
        answers.append(output)

    return " ".join(answers)