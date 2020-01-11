import os

import pandas
import pytest
from random_csv.ClassColumn import ClassColumn
from random_csv.CsvGenerator import CsvGenerator
from random_csv.IntColumn import IntColumn
from random_csv.RandomNumberColumn import RandomNumberColumn
from random_csv.StringColumn import StringColumn

from definitions import OUT_DIR


@pytest.fixture
def generator(monkeypatch):
    generator = CsvGenerator()
    generator.add_column(IntColumn('Integers', start=1))
    generator.add_column(StringColumn('Names'))
    generator.add_column(ClassColumn('Class', ['A', 'B', 'C'], random_state=42))
    generator.calculate_column('Calculated', ['Integers', 'Class'], lambda number, cls: cls * number)
    generator.add_column(RandomNumberColumn('Random', low=5, high=10, digits=1, random_state=42))
    return generator


def test_should_fill_data_frame_with_data_from_columns(generator):
    data_frame = generator.generate_data_frame(5)

    integers = data_frame['Integers']
    for i in range(5):
        assert integers.at[i] == i + 1

    names = data_frame['Names']
    assert names.at[0] == 'Hannes'
    assert names.at[1] == 'Charlos'
    assert names.at[2] == 'İbrahim'

    classes = data_frame['Class']
    assert classes.at[0] == 'C'
    assert classes.at[1] == 'A'
    assert classes.at[2] == 'C'
    assert classes.at[3] == 'C'
    assert classes.at[4] == 'A'

    calculated = data_frame['Calculated']
    assert calculated[0] == 'C'
    assert calculated[1] == 'AA'
    assert calculated[2] == 'CCC'
    assert calculated[3] == 'CCCC'
    assert calculated[4] == 'AAAAA'

    random = data_frame['Random']
    assert random[0] == 6.9
    assert random[1] == 9.8
    assert random[2] == 8.7
    assert random[3] == 8.0
    assert random[4] == 5.8


def test_prints_csv(generator):
    generator.create_csv(5, 'test.csv')

    csv = pandas.read_csv(os.path.join(OUT_DIR, 'test.csv'))
    assert csv.equals(generator.generate_data_frame(5))
