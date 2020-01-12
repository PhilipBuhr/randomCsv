if __name__ == '__main__':
    import time

    from randomcsv import *

    generator = CsvGenerator(out_dir='output')
    generator.add_column(StringColumn("Names"))
    generator.add_column(IntColumn("Integers", start=1))
    generator.add_column(RandomNumberColumn("Random"))
    generator.add_column(CategoryColumn("Categories", [1, 2, 3, 4]))
    generator.calculate_column("Calculated", ["Integers", "Categories"],
                               lambda number, category: f'{number} {category}')

    start = time.time()
    count = 1000
    generator.create_csv(count, 'example.csv')
    print(f'Finished, time elapsed: {time.time() - start} for {count}')
