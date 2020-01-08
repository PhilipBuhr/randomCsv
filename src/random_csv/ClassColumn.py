import random

from pandas import Series

from src.random_csv.Column import Column


class ClassColumn(Column):
    def __init__(self, name, classes, dtype='object'):
        super().__init__(name, dtype)
        self.classes = classes

    def generate_entries(self, count):
        return Series(self.create_data(count))

    def create_data(self, count):
        return [random.choice(self.classes) for _ in range(count)]
