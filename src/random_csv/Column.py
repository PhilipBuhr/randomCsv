from abc import ABC, abstractmethod

from numpy.random import RandomState
from pandas import Series


class Column(ABC):
    def __init__(self, name, dtype=None, null_ratio=0, null_element=None, random_state=None):
        self.name = name
        self.dtype = dtype
        self.null_ratio = null_ratio
        self.null_element = null_element
        self.random_state = random_state

    def generate_entries(self, count):
        series = Series(self.create_data_with_null_elements(count))
        if self.dtype:
            return series.astype(self.dtype)
        return series

    def create_data_with_null_elements(self, count):
        data = []
        values = self.create_data(count)
        if self.null_ratio == 0:
            return values
        random_score = RandomState(self.random_state).random(count)
        for value, score in zip(values, random_score):
            data.append(value if score > self.null_ratio else self.null_element)
        return data

    @abstractmethod
    def create_data(self, count):
        pass
