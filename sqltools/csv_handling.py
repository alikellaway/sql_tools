from value_handling import value_reader
from typing import Callable
from pathlib import Path
from csv import reader
from transact import insertion
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def csv_to_inserts(path: str | Path, table_name: str, insertion_func: Callable = insertion) -> str:
    """
    Converts a .csv file into a list of Insert statement strings that can be executed in a SQL Database.
    :param path: The path of the file to convert.
    :param table_name: The name of the table in which to insert.
    :param insertion_func: The function to use to generate the insertion statements i.e. from postgre, or sql?
    :return: A list of insert strings.
    """
    if isinstance(path, str):
        path = Path(path).resolve()
    elif isinstance(path, Path):
        path = path.resolve()
    else:
        raise NotImplemented
    with open(path, 'r') as file:
        csvreader = reader(file)
        fields = csvreader.__next__()
        insert_dicts = []
        for row in csvreader:
            row_dict = {}
            for idx, value in enumerate(row):
                row_dict[fields[idx]] = value_reader(value.lstrip().strip())
            insert_dicts.append(row_dict)

        return list(map(lambda idict: insertion_func(table_name, idict), insert_dicts))
