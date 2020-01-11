from random_csv.ClassColumn import ClassColumn


def test_should_pick_class_at_random():
    column = ClassColumn('Class', ['A', 'B', 'C'], random_state=42)
    series = column.generate_entries(5)
    assert series.at[0] == 'C'
    assert series.at[1] == 'A'
    assert series.at[2] == 'C'
    assert series.at[3] == 'C'
    assert series.at[4] == 'A'


def test_can_set_type_of_classes():
    column = ClassColumn('IntClass', [1, 2, 3], dtype='object', random_state=42)
    series = column.generate_entries(5)
    print(series)
    assert series.at[0] == 3
    assert series.at[1] == 1
    assert series.at[2] == 3
    assert series.at[3] == 3
    assert series.at[4] == 1
