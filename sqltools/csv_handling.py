from value_handling import value_reader
from typing import Callable
from pathlib import Path
from csv import reader
from transact import insertion, update
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class CSVFileWrapper:
    def __init__(self, path: str | Path):
        self.path = handle_path(path)
        self.reader = None
        self.header = None

    def __enter__(self):
        self.csv = open(self.path, 'rt')
        self.csvr = reader(self.csv)
        self.header = self.csvr.__next__

    def __exit__(self):
        self.csv.close()
        self.reader = None
        self.header = None


def handle_path(path: str | Path):
    if isinstance(path, str):
        path = Path(path).resolve()
    elif isinstance(path, Path):
        path = path.resolve()
    else:
        raise NotImplementedError()
    return path


def csv_to_inserts(path: str | Path, table_name: str, insertion_func: Callable = insertion) -> str:
    """
    Converts a .csv file into a list of insert statement strings that can be executed in a SQL Database.
    :param path: The path of the file to convert.
    :param table_name: The name of the table in which to insert.
    :param insertion_func: The function to use to generate the insertion statements i.e. from postgre, or sql?
    :return: A list of insert strings.
    """
    path = handle_path(path)
    with open(path, 'rt') as file:
        csvreader = reader(file)
        fields = csvreader.__next__()
        insert_dicts = []
        for row in csvreader:
            row_dict = {}
            for idx, value in enumerate(row):
                row_dict[fields[idx]] = value_reader(value.lstrip().strip())
            insert_dicts.append(row_dict)

        return list(map(lambda idict: insertion_func(table_name, idict), insert_dicts))
  

# def csv_to_updates(path: str | Path, table_name: str, update_func: Callable = update):
print((handle_path("C:/Users/AlistairKellaway/Downloads/snakes_count_100.csv")))
