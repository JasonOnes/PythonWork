""" more quick refreshers"""


def anti_vowel(x):
    vowels = "aeiou"
    const_str = str()
    for char in x if char not in vowels:
        const_str += char
    print const_str
