import time

from random_csv import *

generator = CsvGenerator()
generator.add_column(StringColumn("Names"))
generator.add_column(IntColumn("Integers", start=1))
generator.add_column(RandomNumberColumn("Random"))
generator.add_column(ClassColumn("Class", [1, 2, 3, 4]))
generator.calculate_column("Calculated", ["Integers", "Class"], lambda n, c: f'{n} {c}')

start = time.time()
count = 300000
generator.create_csv(count, 'example.csv')
print(f'Finished, time elapsed: {time.time() - start} for {count}')
