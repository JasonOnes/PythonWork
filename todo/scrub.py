"""
Write functions that accept 'dirty' string input, and ouputs a human readable value.
Use a combination of python string methods and regular expressions.

Write, test, and refactor as you go.

>>> scrub_numbers('Be9autiful9 i4s be2tter th4an ug42ly')
'Beautiful is better than ugly'

>>> gentle_clean('Explicit_is-better_than -implicit')
'Explicit is better than implicit.'

>>> clean_data('  42Simple-is_better_than-compl9ex   ')
'Simple is better than complex'

>>> some_scrubber('F l a t   i s   b e t t e r   t h a n   n e s t e d . ')
'Flat is better than nested.'

>>> mr_clean('Sparse is better than dense')
' S p a r s e   i s   b e t t e r   t h a n   d e n s e '

>>> ms_clean('Readability counts')
'R9y c4s'

>>> strong_cleaner('Err@#%$ors sho@#$@#$uld nev1!$#@er pass sile&I&&*(ntly')
'Errors should never pass silently'

>>> extracto('1S2pe3cia4l ca5ses ar6ent sp7ecial en8ough to b9reak the r0ules.')
45

>>> extracto('2S4pe6cia8l ca0ses ar2ent sp4ecial en6ough to b8reak the r0ules.')
40

>>> extracto('3S6pe9cia2l ca5ses ar8ent sp1ecial en4ough to b7reak the r0ules.')
45
"""

import re
#import math

def scrub_numbers(x):
    new_list = re.sub('\d', "", x)
    #print(new_list)
    return new_list
def gentle_clean(x):
    new_list = re.sub('[_]', " ", x).sub('[-]', "", x)
    #print(new_list)
    return new_list
#gentle_clean("he-odsf_butter what")

def clean_data(x):
    new_string = re.sub('[_\-]', " ", x)
    result = re.sub('[\d]', "", new_string).strip()
    return result
#clean_data("  Whe-at__eva!I do what 4")

def some_scrubber(x):
    #new_string = re.sub('\w\s', "", x)
    new_string = x[::2]
    new_string = re.sub('(?<=\w)\s', '', x)
    #print(new_string)
    return new_string
#some_scrubber("w h a t   I       d o n t")

def mr_clean(x):
    y = list(x)
    #z = str(y)
    new_string = " ".join(y)

    return new_string
#mr_clean('Sparse is better thatn dense')


def ms_clean(x):
    clean = list()
    new_string = x.split()
    #new_string = re.split('(\w+)', x)
    for word in new_string:
        new_word = word[0] + str(len(word)-2) + word[-1]
        clean.append(new_word)
        cleanest = " ".join(clean)
    return cleanest

#ms_clean('Readability counts')
def strong_cleaner(x):
    ugly_list = ['%','@', '#', '$', '&', '!', '*', '1', '(',')', 'I']
    old_list = list(x)
    new_list = list()
    for char in old_list:
        if char not in ugly_list:
            new_list.append(char)
    new_string = str("".join(new_list))
    return new_string

#strong_cleaner('Err#@%$ors shou#@$%!ld')
def extracto(x):
    new_string = re.sub('\D', "", x)
    nums = list(new_string)
    num_list = list()
    for char in nums:
        num_list.append(int(char))
    total = sum(num_list)
    #print(total)
    return total
    """new_string = str()
    old_list = list(x)
    new_list = list()
    for char in old_list:
        if char in str(range(10)):
            new_list.append(char)
        print(new_list)

    #new_list = sum(old_list)
    #print(new_list)"""

#extracto("what34eva I d8o what I w22ant")
