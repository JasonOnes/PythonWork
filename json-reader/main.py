import json


def lat_long_load(filename):
    with open(filename, 'r') as file:
        data = file.read()
        long_lat = json.loads(data)
        print("Portland is {}".format(long_lat))

lat_long_load('/home/jasonones/Desktop/latfile.txt')
