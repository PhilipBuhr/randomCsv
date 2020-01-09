import os

from random_csv.Column import Column
from random_csv.FileUtils import read_line_looping

from definitions import DICTIONARY_DIR


class StringColumn(Column):

    def __init__(self, name, dictionary='firstNames.txt'):
        super().__init__(name)
        self.dictionary = os.path.join(DICTIONARY_DIR, dictionary)

    def create_data(self, count):
        return read_line_looping(self.dictionary, count)
