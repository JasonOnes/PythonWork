"""
Write a function that quanitifies word occourances in a given string.

>>> quantify_words("Red touching black is a friend of Jack, Red touching yellow can kill a fellow.")
a 2
black 1
can 1
fellow 1
friend 1
is 1
jack 1
kill 1
of 1
red 2
touching 2
yellow 1


>>> quantify_words("In the end, it's concluded that the airspeed velocity of a \
(European) unladen swallow is about 24 miles per hour or 11 meters per second.")
(european) 1
11 1
24 1
a 1
about 1
airspeed 1
concluded 1
end 1
hour 1
in 1
is 1
it's 1
meters 1
miles 1
of 1
or 1
per 2
second 1
swallow 1
that 1
the 2
unladen 1
velocity 1
"""


def quantify_words(x):
    how_many = dict()
    lowcase = x.lower()
    clean_list = lowcase.replace(",", " ").replace(".", " ").replace("\n", "").split()

    for word in clean_list:
        if word in how_many:
            how_many[word] += 1
        else:
            how_many[word] = 1

    for word, how_many[word] in sorted(how_many.items()):
        print(word, how_many[word])

    word_count = {word: how_many[word]}
    from collections import Counter
    c = Counter(word_count.values())
    c.most_common()[-1]

text =""" Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.
Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.
But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth.
"""
quantify_words(text)
