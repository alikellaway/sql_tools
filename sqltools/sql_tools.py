from typing import Any
from pathlib import Path
import csv
import logging
from value_handling import value_reader, value_writer

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def insertion(table_name: str, names_values: dict[str:Any]) -> str:
    """
    Generates an insert statement given a table name and a dictionary mapping the schema 
    to the values to insert.
    :param table_name: The name of the table to insert into.
    :param names_value: A dictionary mapping the names of the columns to the values to insert.
    :return: A string which can be used to insert the values given into a table of name table_name
    into a SQL database.
    """
    def f(collection): return " ".join(
        map(lambda n: f'{value_writer(n)},', collection))[:-1]
    outstr = f'INSERT INTO {table_name} ({f(names_values.keys())})\n'
    outstr += f'VALUES ({f(names_values.values())});'
    return outstr


def proc_call(proc_name: str, names_vals: dict[str:Any]) -> str:
    """
    Generates a string which can be used to execute a procedure of a given name with given parameters.
    :param proc_name: The name of the stored procedure to execute.
    :param names_vals: A dictionary mapping the parameter names to the argument values.
    :return: A string which can be used to call a stored procedure on a SQL database.
    """
    outstr = f'EXEC {proc_name} '
    outstr += " ".join(
        map(lambda kvp: f'@{kvp[0]} = {value_writer(kvp[1])},', names_vals.items()))
    # keyvaluepair
    return outstr[:-1] + ";"


def create_table(table_name: str, col_names_types: dict[str:str]) -> str:
    """
    Creates a strings which can be used to create a table of the given name and types in a SQL database.
    :param table_name: The name to give the table once it's created.
    :param col_names_types: A dictionary mapping the names of the columns to the types of the columns (both strings).
    :return: A string.
    """
    outstr = f'CREATE TABLE {table_name} (\n'
    outstr += "".join(
        map(lambda kvp: f'\t{kvp[0]} {kvp[1]},\n', col_names_types.items()))
    outstr = outstr[:-2] + "\n);"
    return outstr


def drop_table(table_name: str) -> str:
    """
    Creates strings to drop a table from a SQL database.
    :param table_name: The name of the table to drop.
    :return: A string that will drop the table when given to a SQL db.
    """
    return f'DROP TABLE {table_name};'


def update(table_name: str, names_values: dict[str:Any], where: None | Any = None) -> str:
    """
    Generates a string which can be used to update a table of a given name in columns of specified names
    with specified values with a given condition set.
    :param table_name: A string containing the name of the table to update.
    :param names_values: A dictionary mapping the column names to update to the replacement values.
    :param where: A string containing the where condition logic.
    :return: A string which can be used to update a table in a SQL database.
    """
    outstr = f'UPDATE {table_name}\nSET '
    outstr += " ".join(
        map(lambda kvp: f'{kvp[0]} = {value_writer(kvp[1])},', names_values))
    # keyvaluepair
    outstr = outstr[:-1] + (";" if where is None else f'\nWHERE {where};')
    return outstr


def csv_to_inserts(path: str | Path, table_name: str) -> str:
    """
    Converts a .csv file into a list of Insert statement strings that can be executed in a SQL Database.
    :param path: The path of the file to convert.
    :param table_name: The name of the table in which to insert.
    :return: A list of insert strings.
    """
    if isinstance(path, str):
        path = Path(path).resolve()
    elif isinstance(path, Path):
        path = path.resolve()
    else:
        raise NotImplemented
    with open(path, 'r') as file:
        csvreader = csv.reader(file)
        fields = csvreader.__next__()
        insert_dicts = []
        for row in csvreader:
            row_dict = {}
            for idx, value in enumerate(row):
                row_dict[fields[idx]] = value_reader(value.lstrip().strip())
            insert_dicts.append(row_dict)

        return list(map(lambda idict: insertion(table_name, idict), insert_dicts))


if __name__ == '__main__':
    d = {
        "k1": 10,
        "k2": 10.01234,
        "k3": None,
        "k4": "v4"
    }

    t = {
        "PersonID": "int",
        "LastName": "varchar(255)",
        "FirstName": "varchar(255)",
        "Address": "varchar(255)",
        "City": "varchar(255)"
    }

    # print(insertion("table", d))
    # print(proc_call("proc1", d))
    # print(update("table", d, where="X>4"))
    # print(create_table("table1", t))
    # print(value_reader("10.65"))
