from csv import reader
from urllib.request import urlopen
from contextlib import closing
from common.constants import InputCSV
from string import ascii_lowercase


def run(base_path):
    combined_visits = {}
    all_paths = set()

    for c in ascii_lowercase:

        # Read files
        visits = read_file(f'{base_path}{c}.csv')

        for visit in visits:
            all_paths.add(visit.path)
            add_visit(combined_visits, visit.user, visit.path, visit.length)

    return 0


def read_file(url):
    with closing(urlopen(url)) as file:
        csv_file = reader(file.read().decode('utf-8').splitlines())

        # pop the first line to remove the header
        data = list(csv_file)
        data.pop(0)

        return [PathVisit(row[InputCSV.USER_ID], row[InputCSV.PATH], int(row[InputCSV.LENGTH])) for row in data]


def add_visit(final_data, user, path, length):
    if user not in final_data:
        final_data[user] = {}

    if path not in final_data[user]:
        final_data[user][path] = length
    else:
        final_data[user][path] += length


class PathVisit:
    def __init__(self, user, path, length):
        self.user = user
        self.path = path
        self.length = length
