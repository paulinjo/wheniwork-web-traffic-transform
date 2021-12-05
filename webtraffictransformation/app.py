from string import ascii_lowercase

from webtraffictransformation.util.files import read_file, write_file
from webtraffictransformation.util.visits import add_visit


def run(base_input_path, output_file):
    combined_visits = {}
    all_paths = set()

    for c in ascii_lowercase:

        visits = read_file(f'{base_input_path}{c}.csv')

        for visit in visits:
            all_paths.add(visit.path)
            add_visit(combined_visits, visit)

    # Turn the set of paths into a list to ensure stable iteration
    write_file(list(all_paths), combined_visits, output_file)
