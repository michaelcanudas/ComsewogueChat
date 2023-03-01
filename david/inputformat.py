import re
import main

input = "When is the first tennis match? where is it?" #code that takes stuff from website

pattern = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?|\!)\s'

sentences = re.split(pattern, input)

answers = []
for sentence in sentences:
    answers.append(main.answer(sentence))

print(answers)