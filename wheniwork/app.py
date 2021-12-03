from csv import reader
from urllib.request import urlopen
from contextlib import closing
base_path = 'https://public.wiwdata.com/engineering-challenge/data/'
file_name = 'a'


def run():
    # Read files
    with closing(urlopen('https://public.wiwdata.com/engineering-challenge/data/a.csv')) as file:
        csv_file = reader(file.read().decode('utf-8').splitlines())
        data = list(csv_file)
        print(data)

    # Map Reduce
    # Output CSV
    return 0
