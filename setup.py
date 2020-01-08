from glob import glob
from os.path import splitext, basename

from setuptools import setup
from setuptools import find_packages

setup(
    name='randomCsv',
    version='0.1.0',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    url='',
    license='',
    author='Philip Buhr',
    author_email='philip.buhr@buhrwerk.de',
    description='For generating specific CSVs for testing data piplines'
)
