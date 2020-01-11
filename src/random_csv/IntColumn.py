import numpy as np
from random_csv.Column import Column


class IntColumn(Column):
    def __init__(self, name, dtype=None, start=0, null_ratio=0, null_element=np.NAN):
        super().__init__(name, dtype=dtype, null_ratio=null_ratio, null_element=null_element)
        self.start = start

    def create_data(self, count):
        return range(self.start, self.start + count)
