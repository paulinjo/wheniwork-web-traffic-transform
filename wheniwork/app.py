from csv import reader
from itertools import groupby
from urllib.request import urlopen
from contextlib import closing
from common.constants import InputCSV

file_name = 'a'


def run(base_path):
    clean_data = {}

    # Read files
    raw_data = read_file(f'{base_path}a.csv')

    # Map Reduce
    # clean_data = [(row[InputCSV.USER_ID], row[InputCSV.PATH], row[InputCSV.LENGTH]) for row in raw_data]
    # paths = {}
    # grouped = []
    # for k, g in groupby(clean_data, lambda x: x[0]):
    #     print(k)
    #
    # # Output CSV
    return 0


def read_file(url):
    with closing(urlopen(url)) as file:
        csv_file = reader(file.read().decode('utf-8').splitlines())

        # pop the first line to remove the header
        data = list(csv_file)
        data.pop(0)
        return data