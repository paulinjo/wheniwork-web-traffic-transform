from sys import argv
from app import run

DEFAULT_BASE_PATH = 'https://public.wiwdata.com/engineering-challenge/data/'

if __name__ == '__main__':
    path = argv[1] if len(argv) == 2 else DEFAULT_BASE_PATH
    run(path)
