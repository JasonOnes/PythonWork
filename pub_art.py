""" Input user location [maybe use cellphone coordinates] and show closest
    works of public art"""
import csv
import pandas as pandas
#def find_art(x):
    #x = input("Where are you?">> )
#with open('/home/jasonones/Git/PythonFullStack/1_Python/labs/objects/public_art/public_art.csv') as taco:
    #art = csv.DictReader(taco)

    #print(art)
arty = pandas.read_csv('/home/jasonones/Git/PythonFullStack/1_Python/labs/objects/public_art/public_art.csv')
print(arty)
