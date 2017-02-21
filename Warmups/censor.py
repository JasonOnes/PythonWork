""" more warm ups, replacing within strings"""


def censor(text, word):
    if word in text:
        clean = text.replace(word, "*" * len(word))

    print(clean)

censor("What the fuck ever!", "fuck")
