import numpy as np
from randomcsv.CategoryColumn import CategoryColumn


def test_should_pick_class_at_random():
    column = CategoryColumn('Class', ['A', 'B', 'C'], random_state=42)
    series = column.generate_entries(5)
    assert series.at[0] == 'C'
    assert series.at[1] == 'A'
    assert series.at[2] == 'C'
    assert series.at[3] == 'C'
    assert series.at[4] == 'A'


def test_can_set_type_of_classes():
    column = CategoryColumn('IntClass', [1, 2, 3], random_state=42)
    series = column.generate_entries(5)
    assert series.at[0] == 3
    assert series.at[1] == 1
    assert series.at[2] == 3
    assert series.at[3] == 3
    assert series.at[4] == 1


def test_default_null_elements_are_chosen_by_pandas():
    column = CategoryColumn("Category", [1, 2, 3], null_ratio=0.5, random_state=42)
    series = column.generate_entries(5)
    assert np.isnan(series[0])
    assert series[1] == 1
    assert series[2] == 3
    assert series[3] == 3
    assert np.isnan(series[4])


def test_null_elements_can_be_set():
    column = CategoryColumn("Category", [1, 2, 3], null_ratio=0.5, null_element=-1, random_state=42)
    series = column.generate_entries(5)
    assert series[0] == -1
    assert series[1] == 1
    assert series[2] == 3
    assert series[3] == 3
    assert series[4] == -1
