import re
from answer import answer

pattern = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s'

def format(input):
    sentences = re.split(pattern, input)

    answers = []
    for sentence in sentences:
        answers.append(answer(sentence))

    return answers
