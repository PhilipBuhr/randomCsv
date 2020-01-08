import os

from pandas import DataFrame

from definitions import OUT_DIR
from src.random_csv.Column import Column
from src.random_csv.FileWriter import write


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
            columns = [data[source] for source in instruction.source_columns]
            data[instruction.column_name] = instruction.function(*columns)
        return data

    def create_csv(self, count, file_name, delimiter=','):
        data_frame: DataFrame = self.generate_data_frame(count)
        write(file_name, data_frame.to_csv(sep=delimiter, index=False))


class Instruction:
    def __init__(self, column_name, source_columns, function):
        self.column_name = column_name
        self.source_columns = source_columns
        self.function = function
