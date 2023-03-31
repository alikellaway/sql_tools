import transact
import unittest
from sys import path

path.append("sqltools")


class TestTransact(unittest.TestCase):

    def test_insertion(self):
        names_values = {
            "col1": "flash",
            "col2": "batman",
            "col3": "joker",
            "col4": "iceman"
        }
        exp = "INSERT INTO my_table (\"col1\", \"col2\", \"col3\", \"col4\")\nVALUES (\"flash\", \"batman\", \"joker\", \"iceman\");"
        self.assertEqual(transact.insertion("my_table", names_values), exp)

    def test_procedure_call(self):
        params_args = {
            "param1": "arg1",
            "param2": "arg2",
            "param3": "arg3",
            "param4": "arg4",
            "param5": "arg5"
        }
        exp = "EXEC proc_name @param1 = \"arg1\", @param2 = \"arg2\", @param3 = \"arg3\", @param4 = \"arg4\", @param5 = \"arg5\";"
        self.assertEqual(exp, transact.procedure_call())


if __name__ == '__main__':
    unittest.main()
