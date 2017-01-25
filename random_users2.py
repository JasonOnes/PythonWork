import requests
import json
from pprint import pprint as pp


def pretty_results():

    names = requests.get('http://randomuser.me/api/?results=5')

    all_dict_info = json.loads(names.text)
    #print(all_dict_info)

    #print(all_dict_info["results"])
    for person in all_dict_info['results']:

        print("Name: {} {} {}".format(person["name"]["title"], person["name"]["first"], person["name"]["last"]))
        print("Email: {}".format(person["email"]))
        print("Username: {}".format(person["login"]["username"]))
        print("Registration date: {}".format(person["registered"]))
        print("Birth date: {}".format(person["dob"]))
        print()

pretty_results()
