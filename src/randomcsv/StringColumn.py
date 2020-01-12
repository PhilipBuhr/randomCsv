import os

from pkg_resources import resource_filename
from randomcsv.Column import Column
from randomcsv.FileUtils import read_line_looping

DICTIONARY_DIR = resource_filename('randomcsv.resources.dictionaries', '')


class StringColumn(Column):

    def __init__(self, name, dictionary='firstNames.txt', null_ratio=0, null_element=''):
        super().__init__(name)
        self.dictionary = os.path.join(DICTIONARY_DIR, dictionary)
        self.null_ratio = null_ratio
        self.null_element = null_element

    def _create_data(self, count):
        return read_line_looping(self.dictionary, count)
