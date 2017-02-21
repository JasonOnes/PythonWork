""" more quick refreshers"""


def anti_vowel(x):
    vowels = "aeiouAEIOU"
    const_str = str()
    for char in x:
        if char not in vowels:
            const_str += char
    print(const_str)

anti_vowel("Hey Abbie, there baby!")
