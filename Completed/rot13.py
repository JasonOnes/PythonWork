"""
Write a function to decrypt an ROT13 Enconded message.

message = "Ohg, bssvpre, V qvqa'g pngpu gurfr -- gurl ner zl crg svfu naq V whfg\
 oevat gurz urer gb fjvz. Jura gurl'er qbar gurl whzc onpx vagb gur ohpxrg."
"""

# Write your code here
def decode(x):
    lower_m = x.lower()
    char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    master = char * 2
    decoded_x = list()
    for letter in lower_m:
        if letter in char:
            n = char.index(letter)
            decoded_x.extend(master[n+13])

        elif letter not in char:
            decoded_x.extend(letter)
    print(str(decoded_x))

message = "Ohg, bssvpre, V qvqa'g pngpu gurfr -- gurl ner zl crg svfu naq V whfg\
 oevat gurz urer gb fjvz. Jura gurl'er qbar gurl whzc onpx vagb gur ohpxrg."

decode(message)
