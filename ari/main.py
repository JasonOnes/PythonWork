

def choice():
    choice = input("""Compute the readability of one of the texts below:
                    1. geneology-of-morals.txt
                    2. gettysburg-address.txt
                    3. jack-and-jill.txt or
                    4. Quit
                    Give an explicit number!:   """)

    choices = {"1": '/home/jasonones/Git/PythonFullStack/1_Python/labs/projects/ari/books/geneology-of-morals.txt',
               "2": '/home/jasonones/Git/PythonFullStack/1_Python/labs/projects/ari/books/gettysburg-address.txt',
               "3": '/home/jasonones/Git/PythonFullStack/1_Python/labs/projects/ari/books/jack-and-jill.txt',
               "4": '/home/jasonones/Git/guildlab/ari/main.py'
            }
    return choices[choice]

def ari():
    with open(choice(), 'r') as text_to_read:
        readable_text = text_to_read.read()
        list_of_words = readable_text.split(" ")
        list_of_sentences = readable_text.split(".")
        num_of_char = len(readable_text)
        num_of_words = len(list_of_words)
        num_of_sentences = len(list_of_sentences)

        ari_scale = {
                 1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
                 2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
                 3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
                 4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
                 5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
                 6: {'ages': '10-11', 'grade_level':    '5th Grade'},
                 7: {'ages': '11-12', 'grade_level':    '6th Grade'},
                 8: {'ages': '12-13', 'grade_level':    '7th Grade'},
                 9: {'ages': '13-14', 'grade_level':    '8th Grade'},
                10: {'ages': '14-15', 'grade_level':    '9th Grade'},
                11: {'ages': '15-16', 'grade_level':   '10th Grade'},
                12: {'ages': '16-17', 'grade_level':   '11th Grade'},
                13: {'ages': '17-18', 'grade_level':   '12th Grade'},
                14: {'ages': '18-22', 'grade_level':      'College'}
            }

        ari_value = ((num_of_char/num_of_words) * 4.17) + ((num_of_words/num_of_sentences) * 0.5) - 21.43
        clean_ari = int(ari_value)
        if clean_ari > 14:
            clean_ari = 14

        age = ari_scale[clean_ari]['ages']
        grade = ari_scale[clean_ari]['grade_level']

    print('''
          The ARI for the file, {}, is {}.
          This corresponds to a {} level of difficult.
          That is suitable for and average person {} years old.'''.format(text_to_read, clean_ari, grade, age))

ari()
