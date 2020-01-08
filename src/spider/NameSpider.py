import json
import os

import requests

from definitions import ROOT_DIR

names_dictionary_file = os.path.join(ROOT_DIR, 'resources/dictionaries/firstNames.txt')
api_url = 'https://uinames.com/api/'


def getNamesBatch(count=500):
    response = requests.get(f'{api_url}?amount={count}')
    data = json.loads(response.text)
    return data


def print_first_names(names):
    with open(names_dictionary_file, 'w') as file:
        for name in names:
            if name['name'].strip():
                file.write(name['name'] + '\n')


if __name__ == '__main__':
    names = getNamesBatch()
    print_first_names(names)