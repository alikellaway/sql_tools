
def insertion(table_name: str, names_values: dict[str:str] | list[dict[str:str]]) -> str:
    outstr = f'INSERT INTO {table_name}\n'
    if isinstance(names_values, list):
        names = names_values[0].keys()
        values_str = ""
        for d in names_values:
            d_str = " ".join(map(lambda v: f'{v},', d.values()))

            values += f'()'
    else:
        names = names_values.keys()
        values_str = f''
    names_str = " ".join(map(lambda n: f'{n},', names))
    outstr += f'({names_str[:-1]})\nVALUES\n'
    outstr += values_str
    return outstr


if __name__ == '__main__':
    d = {
        "contact_id": "id1",
        "name": "name1",
        "sname": "sname1"
    }
    print(insertion("table1", d))