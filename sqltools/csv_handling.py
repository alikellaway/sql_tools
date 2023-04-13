from value_handling import value_reader
from typing import Callable
from pathlib import Path
from csv import reader
from transact import insertion, update
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class CSVFile:
    def __init__(self, path: str | Path):
        self.path = handle_path(path)
        self.reader = None
        self.header = None
        self.rows = None

    def __enter__(self):
        self.csv = open(self.path, 'rt')
        self.rows = reader(self.csv)
        self.header = self.rows.__next__()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.csv.close()
        self.reader = None
        self.header = None
        self.rows = None


def handle_path(path: str | Path):
    if isinstance(path, str):
        path = Path(path).resolve()
    elif isinstance(path, Path):
        path = path.resolve()
    else:
        raise NotImplementedError()
    return path

    
def csv_to_inserts(path: str | Path, table_name: str, insertion_func: Callable = insertion):
    """
    Converts a .csv file into a list of insert statement strings that can be executed in a SQL Database.
    :param path: The path of the file to convert.
    :param table_name: The name of the table in which to insert.
    :param insertion_func: The function to use to generate the insertion statements i.e. from postgre, or sql?
    :return: A list of insert strings.
    """
    with CSVFile(path) as f:
        insert_strings = []
        for row in f.rows:
            # Create a with values to convert enable insertion convertion
            row_dict = {}
            for idx, value in enumerate(row):
                row_dict[f.header[idx]] = value_reader(value.lstrip().rstrip())
            insert_strings.append(insertion_func(table_name, row_dict))
    return insert_strings
            
    
  

# def csv_to_updates(path: str | Path, table_name: str, update_func: Callable = update):
print((csv_to_inserts2("C:/Users/AlistairKellaway/Downloads/snakes_count_100.csv", table_name="name")))
