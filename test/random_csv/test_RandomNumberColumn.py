from randomcsv.RandomNumberColumn import RandomNumberColumn


def test_fills_column_with_random_numbers():
    column = RandomNumberColumn('Numbers', low=10, high=20, digits=1, random_state=42)
    series = column.generate_entries(3)
    assert series.at[0] == 13.7
    assert series.at[1] == 19.5
    assert series.at[2] == 17.3


def test_all_values_are_between_high_and_low():
    column = RandomNumberColumn('Numbers', low=5, high=10, random_state=None)
    series = column.generate_entries(1000)
    are_between = (series >= 5) & (series < 10)
    assert are_between.all()
