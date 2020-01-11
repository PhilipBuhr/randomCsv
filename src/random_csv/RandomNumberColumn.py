import numpy as np
from numpy.random import RandomState
from random_csv.Column import Column


class RandomNumberColumn(Column):
    def __init__(self, name, low=0, high=1, digits=None, dtype=None, null_ratio=0, null_element=np.NAN,
                 random_state=None):
        """
        Creates a Column with random float numbers between :param low (included) and :param high (excluded)
        If a value for :param digits is provided, the column values will be rounded to the number of digits

        Parameters
        ----------
        :param name: Name of the Column
        :param low: Lower bound for the generated values (included, default 0)
        :param high: Upper bound for the generated values (excluded, default 1)
        :param digits: Number of digits to which the values are rounded, if None values are not rounded
        :param dtype:
        :param null_ratio:
        :param null_element:
        :param random_state:
        """
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
