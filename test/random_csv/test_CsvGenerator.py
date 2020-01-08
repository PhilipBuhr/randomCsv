import os

import pandas
import pytest

from definitions import OUT_DIR
from random_csv.ClassColumn import ClassColumn
from random_csv.CsvGenerator import CsvGenerator
from random_csv.IntColumn import IntColumn
from random_csv.StringColumn import StringColumn
import random


def mock_choice(sequence):
    return sequence[0]


@pytest.fixture
def generator(monkeypatch):
    monkeypatch.setattr(random, 'choice', mock_choice)
    generator = CsvGenerator()
    generator.add_column(IntColumn("Integers"))
    generator.add_column(StringColumn("Names"))
    generator.add_column(ClassColumn("Class", ["A", "B", "C"]))
    generator.calculate_column("Calculated", ["Integers", "Class"], lambda number, cls: cls*(number + 1))
    return generator


def test_should_fill_data_frame_with_data_from_columns(generator):
    data_frame = generator.generate_data_frame(5)

    integers = data_frame['Integers']
    for i in range(5):
        assert integers.at[i] == i

    names = data_frame['Names']
    assert names.at[0] == 'Hannes'
    assert names.at[1] == 'Charlos'
    assert names.at[2] == 'İbrahim'

    classes = data_frame['Class']
    for i in range(5):
        assert classes.at[i] == "A"

    calculated = data_frame['Calculated']
    assert calculated[0] == 'A'
    assert calculated[1] == 'AA'
    assert calculated[2] == 'AAA'
    assert calculated[3] == 'AAAA'
    assert calculated[4] == 'AAAAA'


def test_prints_csv(generator):
    generator.create_csv(5, "test.csv")

    csv = pandas.read_csv(os.path.join(OUT_DIR, "test.csv"))
    assert csv.equals(generator.generate_data_frame(5))
