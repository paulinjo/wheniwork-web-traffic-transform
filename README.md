# When I Work: Web Traffic Transform

## Instalation
This program uses vanilla Python 3. No explicit instalation is required other than Python 3 itself.

## Running
1. Clone the repository
2. From the project root folder run `python3 -m webtraffictransformation`

### Command Line Arguments
* `-i` (`--input`): Set the base URL for the raw traffic files; must include the trailing `/`
  * Default value: https://public.wiwdata.com/engineering-challenge/data/
* `-o` (`--output`): Path and file name for the output .csv
  * Default value: `./output.csv`

### Running tests
From the root directory run `python3 -m unittest discover webtraffictransformation/tests/` 
