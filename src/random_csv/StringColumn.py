import os

from definitions import DICTIONARY_DIR
from src.random_csv.Column import Column


class StringColumn(Column):

    def __init__(self, name, dictionary='firstNames.txt'):
        super().__init__(name)
        self.dictionary = os.path.join(DICTIONARY_DIR, dictionary)

    def create_data(self, count):
        with open(self.dictionary, 'r') as file:
            return [file.readline().strip() for _ in range(count)]
