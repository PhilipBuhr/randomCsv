import os

from random_csv.StringColumn import StringColumn


def mock_join(_, dictionary):
    this_dir = os.path.dirname(os.path.abspath(__file__))
    return f'{this_dir}/{dictionary}'


def test_fills_column_with_names_from_dictionary():
    column = StringColumn('names')
    series = column.generate_entries(3)
    assert series.at[0] == 'Hannes'
    assert series.at[1] == 'Charlos'
    assert series.at[2] == 'İbrahim'


def test_cycles_through_name_dict_entries(monkeypatch):
    monkeypatch.setattr(os.path, 'join', mock_join)
    column = StringColumn('names')
    series = column.generate_entries(4)
    assert series.at[3] == 'Hannes'
