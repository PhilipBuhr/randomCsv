from pandas import Series

from random_csv.Column import Column


class IntColumn(Column):
    def __init__(self, name):
        super().__init__(name, dtype='int64')

    def create_data(self, count):
        return range(count)
