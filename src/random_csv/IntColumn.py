import numpy as np
from random_csv.Column import Column


class IntColumn(Column):
    def __init__(self, name, dtype=None, start=0, null_ratio=0, null_element=np.NAN):
        """
        Used to create Columns with incrementing Integers.
        The default dtype is None because Errors might be raised if null_elements are used.
        A fraction of the elements, determined by null_ratio, will be replaced by the null_element, representing invalid
        entries.

        Keyword arguments:
            dtype : the datatype of the resulting pandas.Series. Per default None (automatically determined by pandas)
            start : start value of the column (included, default 0)
            null_ratio : ratio of elements, which will be replaced by the null_element (default 0.0)
            null_element : value of invalid entries (default numpy's NAN)
        """
        super().__init__(name, dtype=dtype, null_ratio=null_ratio, null_element=null_element)
        self.start = start

    def create_data(self, count):
        return range(self.start, self.start + count)
