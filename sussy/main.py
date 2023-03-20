test_data = [
    {
        "sentence": ["<START>", "when", "is", "the", "next", "tennis", "match", "<END>"],
        "pos": ["<START>", "WRB", "VBZ", "DT", "JJ", "NN", "NN", "<END>"],
        "interpret": ["<START>", "when", "is", "the", "SUBJECT>", "SUBJECT>", "SUBJECT>", "<END>"]
    },
    {
        "sentence": ["<START>", "who", "is", "the", "principal", "of", "jfk", "middleschool", "<END>"],
        "pos": ["<START", "WP", "VBZ", "DT", "NN", "IN", "NN", "NN", "<END>"],
        "interpret": ["<START", "who", "is", "the", "SUBJECT>", "of", "SUBJECT>", "SUBJECT>", "<END>"]
    },
]


def p(pre, tok, pos):
    p_token = 0
    p_context = 0

    count = 0
    for entry in test_data:
        sentence = entry["interpret"]

        if tok in sentence:
            p_token += 1

            index = sentence.index(tok)
            if index - 1 >= 0 and index + 1 < len(sentence):
                if sentence[index - 1] == pre and sentence[index + 1] == pos:
                    p_context += 1

        count += len(sentence)

    return p_context / p_token


sentence = [
    ["when", "WRB"],
    ["is", "VBZ"],
    ["the", "DT"],
    ["next", "JJ"],
    ["girls", "NNS"],
    ["middle", "NN"],
    ["school", "NN"],
    ["lacrosse", "NN"],
    ["game", "NN"]
]

omg = []
for word in sentence:
    if "NN" in word[1] or "JJ" in word[1]:
        omg.append(word[0])



print(omg)
