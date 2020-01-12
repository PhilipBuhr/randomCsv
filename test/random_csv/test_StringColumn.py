import os

import pytest
from randomcsv.StringColumn import StringColumn


def mock_join(_, dictionary):
    this_dir = os.path.dirname(os.path.abspath(__file__))
    return f'{this_dir}/{dictionary}'


@pytest.fixture
def column(monkeypatch):
    monkeypatch.setattr(os.path, 'join', mock_join)
    return StringColumn('names')


def test_fills_column_with_names_from_dictionary(column):
    series = column.generate_entries(3)
    assert series.at[0] == 'Hannes'
    assert series.at[1] == 'Charlos'
    assert series.at[2] == 'İbrahim'


def test_cycles_through_name_dict_entries(column):
    series = column.generate_entries(4)
    assert series.at[3] == 'Hannes'


def test_default_null_value_is_empty_string():
    column = StringColumn('names', null_ratio=1)
    series = column.generate_entries(3)
    assert series.at[0] == ''
    assert series.at[1] == ''
    assert series.at[2] == ''


def test_can_overwrite_null_element():
    column = StringColumn('names', null_ratio=1, null_element='N/A')
    series = column.generate_entries(3)
    assert series.at[0] == 'N/A'
    assert series.at[1] == 'N/A'
    assert series.at[2] == 'N/A'
