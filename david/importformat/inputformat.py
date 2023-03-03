import re
from answer import answer
#from googletrans import Translator

#def translate(text, target_language):
    #translator = Translator()
    #if target_language == "english":
        #translation = translator.translate(text, dest="en")
        #return translation.text
    #elif target_language == "spanish":
        #translation = translator.translate(text, dest="es")
        #return translation.text

pattern = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s'

def format(input, span):
    #if span:
        #input = translate(str(input), "english")

    pastQueries = []
    pastContexts = []

    sentences = re.split(pattern, input)

    answers = []
    for sentence in sentences:
        output, pastQueries, pastContexts = answer(sentence, pastQueries, pastContexts)
        #if span:
            #output = translate(str(output), "spanish")
        answers.append(output)

    return answers

#print(format("a que hora es el juego de futbul americano", True))