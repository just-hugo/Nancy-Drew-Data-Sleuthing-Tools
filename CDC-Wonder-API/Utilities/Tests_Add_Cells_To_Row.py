import unittest
from csv_utilities import Add, Error
from test_data import dummy_spreadsheet_input_data
from assertions import Assert
from actions import Action

add = Add()
assertion = Assert()
data = dummy_spreadsheet_input_data
error = Error()
action = Action()


class AddCellsToRow(unittest.TestCase):

    def test_adds_a_dictionary_value_to_a_list(self):
        """
        add.cells_to_row() will add a dictionary value to a list.
        """
        # Test setup
        cells = data.cell_value_dict

        # Test action
        row = add.cells_to_row(cells)

        # Test verification
        assertion.row_contains_cell(data.cell_value_dict["cell_name"], row)

    def test_adds_multiple_dictionary_values_to_a_list(self):
        """
        add.cells_to_row() will add more than one dictionary value to a list.
        """
        # Test setup
        cells = data.cell_values_dict

        # Test action
        row = add.cells_to_row(cells)

        # Test verification
        self.assertEqual(len(row), 3)

    def test_takes_a_dict_as_primary_argument(self):
        """
        add.cells_to_row() will accept a dictionary as its argument.
        """
        # Test setup
        cells = data.cell_values_dict

        # Test action
        add.cells_to_row(cells)

        # Test verification
        assertion.value_type_is(cells, dict)

    def test_cannot_take_string_as_primary_argument(self):
        """
        add.cells_to_row_by_selector() will return a TypeError when a string is passed as the primary argument.
        """

        # Test setup
        cell = data.test_string

        # Test action
        try:
            add.cells_to_row(cell)
            raise AssertionError("Function worked when it shouldn't. It cannot accept a string as an argument.")

        # Test verification
        except TypeError:
            assertion.exception_is_raised(TypeError)

    def test_cannot_take_list_as_primary_argument(self):
        """
        add.cells_to_row_by_selector() will throw a TypeError when a list is passed as the primary argument.
        """

        # Test setup
        cell = []

        with self.assertRaises(TypeError) as triggered_error:
            # Test action
            add.cells_to_row(cell)

        # Test verification
        triggered_error = str(triggered_error.exception)

        self.assertIn(f"Cell argument cannot be a {type(cell)}", triggered_error)

    def test_cannot_take_integer_argument(self):
        """
        """

        cell = 1

        with self.assertRaises(TypeError) as triggered_error:
            # Test action
            add.cells_to_row(cell)

        # Test verification
        triggered_error = str(triggered_error.exception)

        self.assertIn(f"Cell argument cannot be a {type(cell)}", triggered_error)

    def test_returns_list(self):
        """
        add.cells_to_row_by_selector() takes a dictionary argument and returns a list of all the dictionary values.
        """

        # Test setup
        cells = {'cell_1': 'some.selector'}

        # Test action
        row = add.cells_to_row(cells)

        # Test verification
        assertion.value_type_is(row, list)

    def test_returned_list_contains_only_strings(self):
        """
        """

        # Test setup
        cells = data.cell_values_dict

        # Test action
        returned_list = add.cells_to_row(cells)

        # Test verification
        for each_item in returned_list:
            assertion.value_type_is(each_item, str)

    # might be redundant with line 9
    def test_returned_list_contains_new_cell(self):
        return

    def test_missing_argument_throws_error(self):
        """
        """

        # Test setup

        # Test action

        # Test verification

    def test_incorrect_argument_type_throw_error(self):
        return


if __name__ == '__main__':
    unittest.main()
