from abc import ABC, abstractmethod

from pandas import Series


class Column(ABC):
    def __init__(self, name, dtype=None):
        self.name = name
        self.dtype = dtype

    def generate_entries(self, count):
        series = Series(self.create_data(count))
        if self.dtype:
            return series.astype(self.dtype)
        return series

    @abstractmethod
    def create_data(self, count):
        pass
