from typing import Any
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


def update(table: str, set: dict[str:Any], where: str = None, order: str = None, limit: int = None, offset: int = None):
    outstr = f'UPDATE {table}'
    # set
    outstr += f'\nSET '
    outstr += "\n    ".join(map(lambda kvp: f'{kvp[0]} = {write_val(kvp[1])}', set.items()))
    # where
    outstr += "" if where is None else f"\nWHERE {where}"
    return outstr + ";"


if __name__ == '__main__':
    # print(insert("table_name", {'param1':200, 'param2': 20.8}))
    print(update("table", {"col1": "val1", "col2": "Val2"}, where="some conditional"))