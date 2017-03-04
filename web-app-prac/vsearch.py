""" Searches phrases for letters of words."""


def search_word(phrase: str, letters: str='aeiou') -> set:
    print(set(letters).intersection(set(phrase)))
    return set(letters).intersection(set(phrase))

# search_word("Whateva, I do what I want", "z")
