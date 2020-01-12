import os

import pandas
import pytest
from randomcsv.CategoryColumn import CategoryColumn
from randomcsv.CsvGenerator import CsvGenerator
from randomcsv.IntColumn import IntColumn
from randomcsv.RandomNumberColumn import RandomNumberColumn
from randomcsv.StringColumn import StringColumn


@pytest.fixture
def generator(monkeypatch, tmpdir):
    output_dir = tmpdir.mkdir('output')
    generator = CsvGenerator(out_dir=output_dir)
    generator.add_column(IntColumn('Integers', start=1))
    generator.add_column(StringColumn('Names'))
    generator.add_column(CategoryColumn('Class', ['A', 'B', 'C'], random_state=42))
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


def test_prints_csv(generator, tmpdir):
    file = os.path.join(tmpdir.dirname, tmpdir.basename, 'output/test.csv')
    generator.create_csv(5, 'test.csv')

    csv = pandas.read_csv(file)
    csv['Class'] = csv['Class'].astype('category')
    data_frame = generator.generate_data_frame(5)
    assert csv.equals(data_frame)
