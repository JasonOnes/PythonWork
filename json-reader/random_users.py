import requests
import json

def pretty_results():

    names = request:('http://randomuser.me/api/?users=5')
    dict_info = json.loads(names)
    print(dict_info)

pretty_results()
