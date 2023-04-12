import logging
from typing import Any

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

NULL_SET = ("NONE", "NULL")


def value_writer(value: Any) -> str:
    """
    Takes an object and converts it into a string which a SQL compiler could interpret.
    :param value: A Python object which is to be converted into a string.
    :return: A string representation of an object which can be understood by a SQL compiler.
    """
    if value is None or value == "NULL":
        return "NULL"
    if isinstance(value, str):
        return f'"{value}"'
    if isinstance(value, int) or isinstance(value, float):
        return f'{value}'
    raise NotImplemented("Unable to handle input of type: " + str(type(value)))


def value_reader(value: str) -> Any:
    """
    Aims to read strings from csv files and convert them into Python object for correct operation.
    :param value: The string to attempt to convert.
    :return: A python object representing the input value, if possible and supported.
    """
    if not isinstance(value, str):
        return value
    # If some null entity.
    if value.upper() in NULL_SET:
        return None
    # Try int conversion
    try:
        return int(value)
    except ValueError:
        logger.debug(f'Failed to convert {value} to int.')
    # Try float conversion
    try:
        return float(value)
    except ValueError:
        logger.debug(f'Failed to convert {value} to float.')

    return value


if __name__ == '__main__':
    print(value_reader("NULL"))
