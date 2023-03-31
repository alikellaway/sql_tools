from value_handling import value_reader, value_writer

def insertion(table_name: str, names_values: dict[str:str] | list[dict[str:str]]) -> str:
    outstr = f'INSERT INTO {table_name}\n'
    args_serialise = lambda value_dict: " ".join(map(lambda v: f'{value_writer(v)},', value_dict.values()))[:-1]
    if isinstance(names_values, list):
        names = names_values[0].keys()
        values_str = ""
        for d in names_values:
            values_str += f'({args_serialise(d)}),\n'
    elif isinstance(names_values, dict):
        names = names_values.keys()
        values_str = f'({args_serialise(names_values)}),\n'
    names_str = " ".join(map(lambda n: f'{n},', names))
    outstr += f'({names_str[:-1]})\nVALUES\n'
    outstr += values_str[:-2] + ";"
    return outstr


if __name__ == '__main__':

    d = {
        "contact_id": "id1",
        "name": "name1",
        "sname": "sname1"
    }
    dl = [d, d, d, d]
    print(insertion("table1", d))