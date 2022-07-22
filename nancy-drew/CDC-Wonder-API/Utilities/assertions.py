import unittest


class Assert(unittest.TestCase):

    def row_contains_cell(self, cell: str, row: list):
        return self.assertIn(cell, row)

    def value_type_is(self, value, expected_type):
        return self.assertIs(type(value), expected_type)

    def exception_is_raised(self, expected_exception):
        return self.assertRaises(expected_exception)
