from src.random_csv.StringColumn import StringColumn


def test_fills_column_with_names_from_dictionary():
    column = StringColumn("names")
    series = column.generate_entries(3)
    assert series.at[0] == 'Hannes'
    assert series.at[1] == 'Charlos'
    assert series.at[2] == 'İbrahim'
