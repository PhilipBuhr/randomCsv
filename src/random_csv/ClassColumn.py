from numpy.random import RandomState

from pandas import Series

from random_csv.Column import Column


class ClassColumn(Column):
    def __init__(self, name, classes, dtype='object', random_state=None):
        super().__init__(name, dtype, random_state=random_state)
        self.classes = classes

    def generate_entries(self, count):
        return Series(self.create_data(count))

    def create_data(self, count):
        return RandomState(seed=self.random_state).choice(self.classes, size=count)
