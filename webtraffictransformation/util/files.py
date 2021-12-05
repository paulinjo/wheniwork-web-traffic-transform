from contextlib import closing
from csv import reader, writer
from urllib.request import urlopen

from webtraffictransformation.util.constants import InputCSV
from webtraffictransformation.util.visits import PathVisit


def read_file(url):
    with closing(urlopen(url)) as file:
        csv_file = reader(file.read().decode('utf-8').splitlines())

        # pop the first line to remove the header
        data = list(csv_file)
        data.pop(0)

        return [PathVisit(row[InputCSV.USER_ID], row[InputCSV.PATH], int(row[InputCSV.LENGTH])) for row in data]


def write_file(paths, combined_visits, output_file):
    with open(f'{output_file}', 'w') as csv_file:
        csv_writer = writer(csv_file)

        csv_writer.writerow(['user_id', *paths])
        for user_id, visits in combined_visits.items():
            row = [user_id]
            for path in paths:
                row.append(visits.get(path, 0))
            csv_writer.writerow(row)
