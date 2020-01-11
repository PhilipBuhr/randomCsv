import numpy as np
from random_csv.Column import Column
from numpy.random import RandomState


class RandomNumberColumn(Column):
    def __init__(self, name, low=0, high=1, digits=None, dtype=None, null_ratio=0, null_element=np.NAN, random_state=None):
        super().__init__(name, dtype=dtype, null_ratio=null_ratio, null_element=null_element, random_state=random_state)
        self.low = low
        self.high = high
        self.digits = digits

    def create_data(self, count):
        return [self.map_to_range(rnd) for rnd in RandomState(seed=self.random_state).random(count)]

    def map_to_range(self, rnd):
        value = self.low + (self.high - self.low) * rnd
        if self.digits:
            return round(value, self.digits)
        return value
