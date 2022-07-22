import unittest
from csv_utilities import Add
from assertions import Assert
from test_data import dummy_spreadsheet_input_data

add = Add()
data = dummy_spreadsheet_input_data()
assertion = Assert()


class AddCellToRow(unittest.TestCase):

    def test_adds_a_cell_to_empty_row(self):
        """
        add.cell_to_row() takes a string (cell) and adds it to a list (row).
        """

        # Test setup
        cell = data.cell_values["string"]
        row = data.row_values["empty_row"]

        # Test action
        add.cell_to_row(cell, row)

        # Test verification
        assertion.row_contains_cell(cell, row)

    def test_add_a_cell_to_prepopulated_row(self):
        """
        add.cell_to_row() can add a new cell to a row that is already populated with one or more cells.
        """

        # Test setup
        cell = data.cell_values["string"]
        row = data.row_values["prepopulated_row"]

        # Test action
        add.cell_to_row(cell, row)

        # Test verification
        assertion.row_contains_cell(cell, row)

    def test_does_not_overwrite_prepopulated_row_data_with_new_cell_data(self):
        """
        will not replace existing cell data in a row.
        Will instead add new cells to the end of a row that is already populated with one or more cells."""
        return

    def test_takes_string_as_first_argument(self):
        """
        add.cell_to_row() takes a string (cell) as the first argument.
        """

        # Test setup
        cell = data.cell_values["string"]
        row = data.row_values["empty_row"]

        # Test action
        add.cell_to_row(cell, row)

        # Test verification
        assertion.value_type_is(row[0], str)

    def test_takes_list_as_first_argument(self):
        """
        add.cell_to_row() can take a list as the first argument to populate multiple cells across a row.

        This functionality is similar to copy-and-pasting a whole row in a spreadsheet.
        """

        # Test setup
        cell = data.cell_values["list_of_strings"]
        row = data.row_values["empty_row"]

        # Test action
        add.cell_to_row(cell, row)

        # Test verification
        assertion.value_type_is(cell, list)

    def test_cannot_take_dict_as_first_argument(self):
        """
        add.cell_to_row() will return a TypeError when a dictionary is passed as the first argument.
        """

        # Test setup
        cell = data.cell_values["dictionary"]
        row = data.row_values["empty_row"]

        # Test action
        try:
            if add.cell_to_row(cell, row):
                raise AssertionError("Function worked when it shouldn't. It cannot accept a dictionary as an argument.")

        # Test verification
        except TypeError:
            assertion.exception_is_raised(TypeError)

    def test_cannot_take_int_as_first_argument(self):
        """
        add.cell_to_row() will return a TypeError when an integer value is passed as the first argument.
        """
        # Test setup
        cell = data.cell_values["integer"]
        row = data.row_values["empty_row"]

        # Test action
        try:
            add.cell_to_row(cell, row)
            raise AssertionError("Function worked when it shouldn't. It cannot accept an integer as an argument.")

        # Test verification
        except TypeError:
            assertion.value_type_is(cell, int)

    def test_takes_list_as_second_argument(self):
        """
        add.cell_to_row() can take a list as its second argument, and will then add new entries and return the updated list.
        """
        # Test setup
        cell = data.cell_values["string"]
        row = data.row_values["empty_row"]

        # Test action
        add.cell_to_row(cell, row)

        # Test verification
        assertion.value_type_is(row, list)

    def test_cannot_take_dict_as_second_argument(self):
        """
        add.row_to_cell() will throw an AttributeError if a dictionary is passed as the second argument.
        """
        # Test setup
        cell = data.cell_values["string"]
        row = data.row_values["dict_as_row"]

        # Test action
        try:
            add.cell_to_row(cell, row)
            raise AssertionError("Function worked when it shouldn't. It cannot accept a dictionary as an argument.")

        # Test verification
        except AttributeError:
            assertion.value_type_is(row, dict)

    def test_returns_list(self):
        """
        add.cell_to_row() will return a list after operating on its arguments.
        """

        # Test setup
        cell = data.cell_values["string"]
        row = data.row_values["empty_row"]

        # Test action
        updated_row = add.cell_to_row(cell, row)

        # Test verification
        assertion.value_type_is(updated_row, list)

    def test_returned_list_contains_only_strings(self):
        """
        add.cell_to_row() will always return lists of one or more strings
        """

        # Test data
        cell = data.cell_values["string"]
        row = data.row_values["empty_row"]

        # Test action
        add.cell_to_row(cell, row)

        # Test verification
        for each_cell in row:

            assertion.value_type_is(each_cell, str)

    def test_returned_list_contains_new_cell(self):
        """
        add.cell_to_row() will always return a list that contains the cell data used as its first argument.
        """

        # Test setup
        cell = data.cell_values["string"]
        row = data.row_values["empty_row"]

        # Test action
        returned_list = add.cell_to_row(cell, row)

        # Test verification
        assertion.row_contains_cell(cell, returned_list)

    def test_missing_argument_throws_error(self):
        """
        add.cell_to_row() requires 2 arguments: a cell (string or list) and a row (list).

        Missing arguments will generate a TypeError, like the one caught and asserted on below.
        """
        # Test setup
        cell = data.cell_values["string"]

        # Test action
        try:
            add.cell_to_row(cell)

        # Test verification
        except Exception as e:
            assertion.exception_is_raised(TypeError)

if __name__ == '__main__':
    unittest.main()
