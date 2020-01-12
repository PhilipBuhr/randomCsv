from glob import glob
from os.path import splitext, basename

from setuptools import find_packages
from setuptools import setup

setup(
    name='randomcsv',
    version='0.1.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    package_data={'randomcsv': ['src/randomcsv/resources/dictionaries/*.txt']},
    include_package_data=True,
    url='https://github.com/PhilipBuhr/randomCsv',
    download_url='https://github.com/PhilipBuhr/randomCsv/archive/0.1.0.tar.gz',
    license='MIT',
    author='Philip Buhr',
    author_email='philip.buhr@buhrwerk.de',
    description='For generating specific CSVs for testing data piplines',
    install_requires=['pandas', 'requests', 'pytest', 'numpy']
)
