import random

from random_csv.ClassColumn import ClassColumn


def mock_choice(sequence):
    return sequence[1]


def test_should_pick_class_at_random(monkeypatch):
    monkeypatch.setattr(random, 'choice', mock_choice)
    column = ClassColumn('Class', ['A', 'B', 'C'])
    series = column.generate_entries(5)
    for i in range(5):
        assert series.at[i] == 'B'


def test_can_set_type_of_classes(monkeypatch):
    monkeypatch.setattr(random, 'choice', mock_choice)
    column = ClassColumn('IntClass', [1, 2, 3], dtype='object')
    series = column.generate_entries(5)
    for i in range(5):
        assert series.at[i] == 2
