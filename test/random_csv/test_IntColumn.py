import numpy as np
from random_csv.IntColumn import IntColumn


def test_generates_incrementing_integer_column():
    column = IntColumn('Integers')
    series = column.generate_entries(5)
    for i in range(5):
        assert series.at[i] == i


def test_generates_incrementing_integer_column_with_start_value():
    column = IntColumn('Integers', start=4)
    series = column.generate_entries(3)
    assert series.at[0] == 4
    assert series.at[1] == 5
    assert series.at[2] == 6


def test_default_null_value_is_NaN():
    column = IntColumn('Integers', null_ratio=1)
    series = column.generate_entries(3)
    assert np.isnan(series.at[0])
    assert np.isnan(series.at[1])
    assert np.isnan(series.at[2])


def test_can_overwrite_null_element():
    column = IntColumn('Integers', null_ratio=1, null_element=0, start=5)
    series = column.generate_entries(3)
    assert series.at[0] == 0
    assert series.at[1] == 0
    assert series.at[2] == 0
