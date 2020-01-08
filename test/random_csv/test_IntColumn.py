from pandas import Series

from random_csv.IntColumn import IntColumn


def test_generates_incrementing_integer_column():
    column = IntColumn("Integers")
    series = column.generate_entries(5)
    for i in range(5):
        assert series.at[i] == i
