import unittest
from sys import path

path.append("sqltools")

import transact


class TestTransact(unittest.TestCase):

    def test_insertion(self):
        names_values = {
            "col1": "flash",
            "col2": "batman",
            "col3": "joker",
            "col4": "iceman"
        }
        output = transact.insertion("my_table", names_values)
        exp = "INSERT INTO my_table (\"col1\", \"col2\", \"col3\", \"col4\")\nVALUES (\"flash\", \"batman\", \"joker\", \"iceman\");"
        print(output)
        print(exp)
        assert output == exp

    def test_procedure_call(self):
        params_args = {
            "param1": "arg1",
            "param2": "arg2",
            "param3": "arg3",
            "param4": "arg4",
            "param5": "arg5"
        }
        output = transact.procedure_call()


if __name__ == '__main__':
    unittest.main()
