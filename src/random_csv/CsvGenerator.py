from pandas import DataFrame

from random_csv.Column import Column
from random_csv.FileUtils import write


class CsvGenerator:

    def __init__(self):
        self.columns = []
        self.instructions = []

    def add_column(self, column: Column):
        self.columns.append(column)

    def calculate_column(self, column_name, source_columns, function):
        self.instructions.append(Instruction(column_name, source_columns, function))

    def generate_data_frame(self, count):
        data = DataFrame()
        for column in self.columns:
            data[column.name] = column.generate_entries(count)
        for instruction in self.instructions:
            data[instruction.column_name] = data.apply(instruction.create_row_function(), axis=1)
        return data

    def create_csv(self, count, file_name, delimiter=','):
        data_frame: DataFrame = self.generate_data_frame(count)
        write(file_name, data_frame.to_csv(sep=delimiter, index=False))


class Instruction:
    def __init__(self, column_name, source_columns, function):
        self.column_name = column_name
        self.source_columns = source_columns
        self.function = function

    def create_row_function(self):
        def row_function(row):
            arguments = [row[source] for source in self.source_columns]
            return self.function(*arguments)

        return row_function


def __extract_arguments(row, source_columns):
    return [row[column] for column in source_columns]
