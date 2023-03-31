from value_handling import value_writer
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def insertion(table_name: str, names_values: dict[str:str] | list[dict[str:str]]) -> str:
    """
    Generates an insert statement for a postgre sql database.
    :param table_name: The name of the table to insert into.
    :param names_values: A dictionary or list of dictionaries with names of the columns and the values mapped to each column.
    :return: A string insert statement able to insert the given information.
    """
    outstr = f'INSERT INTO {table_name}\n'
    def args_serialise(value_dict): return ", ".join(
        map(lambda v: f'{value_writer(v)}', value_dict.values()))
    if isinstance(names_values, list):
        names = names_values[0].keys()
        values_str = ", \n\t".join(
            map(lambda d: f'({args_serialise(d)})', names_values))
    elif isinstance(names_values, dict):
        names = names_values.keys()
        values_str = f'({args_serialise(names_values)})'
    names_str = ", ".join(map(lambda n: f'{n}', names))
    outstr += f'\t{table_name}({names_str})\nVALUES\n\t{values_str};'
    logging.debug(f'Created {__name__} insertion:\n{outstr}')
    return outstr


def update(table_name: str, names_values: dict[str:str], where: str = None) -> str:
    """
    Generates an update statement for a postgre sql database.
    :param table_name: The name of the table to update.
    :param names_values: A dict mapping the names of the columns to update to the values to update them to.
    :param where: A string of conditionals which will be used to filter the tuples to update.
    :return: A string that can be used to update the table <table_name> with the values given in a postgre db.
    """
    outstr = f'UPDATE {table_name}\nSET '
    outstr += ",\n    ".join(
        map(lambda kvp: f'{kvp[0]} = {value_writer(kvp[1])}', names_values.items()))
    if where is not None:
        outstr += f'\nWHERE {where};'
    logger.debug(f'Created {__name__} update:\n{outstr}')
    return outstr


def create_table(table_name: str, names_types: dict[str:str]) -> str:
    outstr = f'CREATE TABLE {table_name} ('
    outstr += ",\n\t".join(
        map(lambda kvp: f'{kvp[0]} {kvp[1]}', names_types.items())) + "\n);"
    logger.debug(f'Created {__name__} table creator:\n{outstr}')
    return outstr


def procedure_call(proc_name: str, param_args: dict[str:str]) -> str:
    outstr = f'CALL {proc_name}({", ".join(map(lambda kvp: value_writer(kvp[1]), param_args.items()))});'
    logging.debug(f'Created {__name__} proceduce call:\n{outstr}')
    return outstr


if __name__ == '__main__':
    d = {
        "contact_id": "id1",
        "name": "name1",
        "sname": "sname1"
    }
    dl = [d, d, d, d]
    # print(update("table1", d))
    # print(insertion("table2", d))
    # print(procedure_call("proc_name", d))
    # print(create_table("table1", d))
