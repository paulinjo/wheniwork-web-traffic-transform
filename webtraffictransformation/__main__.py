from argparse import ArgumentParser

from webtraffictransformation.app import run

DEFAULT_INPUT_PATH = 'https://public.wiwdata.com/engineering-challenge/data/'
DEFAULT_OUTPUT_FILE = './output.csv'

parser = ArgumentParser()
parser.add_argument('--input', '-i', help='The input path for the files to parse. Must include the trailing "/"',
                    default=DEFAULT_INPUT_PATH)
parser.add_argument('--output', '-o', help='Path and file name for the output .csv', default=DEFAULT_OUTPUT_FILE)

if __name__ == '__main__':
    args = parser.parse_args()
    run(args.input, args.output)
