# RandomCSV

This library let's you generate CSV files with a specific structure, but 
random data. These CSVs can be used as test data when developing data pipelines.

## Usage
```python
generator = CsvGenerator()

# adds a column filled with integers, starting at 0, incrementing
generator.add_column(IntColumn("Integers"))  

# adds a column filled with strings, currently first names from the firstNames.txt dictionary
generator.add_column(StringColumn("Names"))

# adds a column, values are randomly picked from the provided list
generator.add_column(ClassColumn("Class", ["A", "B", "C"]))

# adds a column with name "Calculated", based on Columns Integers and Class
# the arguments of the given function must match order and type of the values of the columns
generator.calculate_column("Calculated", ["Integers", "Class"], lambda number, cls: cls*(number + 1))

# creates pandas DataFrame with 5 rows
data_frame = generator.generate_data_frame(5) 
# creates CSV file in directory "output"
generator.create_csv(5, "test.csv")
```
