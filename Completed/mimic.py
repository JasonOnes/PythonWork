import random
import re

"""
def clean(dirty_list):
    clean_list = re.sub('\W', '', dirty_list)
    return clean_list
"""
def mimic(filename):
    mimic_list = list()
    mimic_dict = dict()
    #clean(filename)
    with open(filename, 'r') as new_text:
        #scrub = clean(filename)
        scrub = new_text.read().lower().replace(".", "").replace(",", "").split()
        #scrub = re.sub('\W', '', new_text)
        for word in scrub:
            if word in mimic_dict:
                continue
            else:
                mimic_list.append(word)

        for index, word in enumerate(scrub):
            trailing_words = scrub[index+1:index+4]
            mimic_dict.update({word : trailing_words})

    #print(mimic_dict)
    rand_keys = random.sample(mimic_dict.keys(), 1)
    for k in rand_keys:
        #import pdb; pdb.set_trace()
        try:
            selection = random.sample(mimic_dict[k], 3)
            print(rand_keys + selection)
        except ValueError:
            print("Too few to choose from")
            pass
        #try and except ValueError Sample larger than population
        #print(rand_keys + selection)

mimic('/home/jasonones/Git/PythonFullStack/1_Python/labs/projects/ari/books/jack-and-jill.txt')
