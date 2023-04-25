from typing import Any, Iterable
from sqlstrings.value_handling import write_val


def insert(table_name: str, name_value: dict[str:Any]) -> str:
    """
    Generates a string that can be used to insert values into a sqlite database.
    :param table_name: The name of the table to insert into.
    :param name_value: A dict mapping parameter names to their respective values.
    :return: A insert statement string that can be used to insert data insto a sqlite db.
    """
    outstr = f"INSERT INTO {table_name} ({', '.join(name_value.keys())})"
    outstr += f"\nVALUES ({', '.join(map(write_val, name_value.values()))})"
    return outstr + ";"


def inserts(table_name: str, name_values: Iterable[dict[str:Any]]) -> str:
    """
    Generates a string that can be used to insert multiple rows into a sqlite database.
    :param table_name: The name of the table to insert into.
    :param name_values: An iterable containing dictionaries mapping the names of each column 
    to the value to fill it with.
    :return: A string representation that can be used to insert the data.
    """
    outstr = f"INSERT INTO {table_name} ({', '.join(name_values[0].keys())})"
    outstr += f"\nVALUES\n\t"
    outstr += ",\n\t".join(
        map(lambda d: f'({", ".join(map(write_val, d.values()))})', name_values))
    return outstr + ";"


def update(table: str, set: dict[str:Any], where: str = None, order: str = None, limit: int = None, offset: int = None):
    outstr = f'UPDATE {table}'
    # set
    outstr += f'\nSET '
    outstr += "\n    ".join(
        map(lambda kvp: f'{kvp[0]} = {write_val(kvp[1])}', set.items()))
    # where
    outstr += "" if where is None else f"\nWHERE {where}"
    return outstr + ";"


if __name__ == '__main__':
    # print(insert("table_name", {'param1':200, 'param2': 20.8}))
    # print(update("table", {"col1": "val1", "col2": "Val2"}, where="some conditional"))
    d = {
        'k1': 'v1',
        'k2': 'v2',
        'k3': 'v3',
        'k4': 'v4'
    }
    print(inserts("name", [d, d, d]))
