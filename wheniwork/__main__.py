from sys import argv
from app import run

DEFAULT_INPUT_PATH = 'https://public.wiwdata.com/engineering-challenge/data/'
DEFAULT_OUTPUT_FILE = './output.csv'

if __name__ == '__main__':
    input_path = argv[1] if len(argv) >= 2 else DEFAULT_INPUT_PATH
    output_file = argv[2] if len(argv) >= 3 else DEFAULT_OUTPUT_FILE
    run(input_path, output_file)
