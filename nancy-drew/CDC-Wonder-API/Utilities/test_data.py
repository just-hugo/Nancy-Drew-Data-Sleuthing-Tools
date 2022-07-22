import unittest


class dummy_spreadsheet_input_data(unittest.TestSuite):

    row_values = {
        "empty_row": [],
        "prepopulated_row": ["test_entry_in_list"],
        "dict_as_row": {}
    }

    cell_values = {
        "string": "Lorem ipsum dolor sit amet.",
        "integer": 1,
        "dictionary": {},
        "list_of_strings": ["string_1", "string_2"]
    }

    cell_value_dict = {
        "cell_name": "Lorem ipsum dolor sit amet."
    }

    cell_values_dict = {
        "first_cell_name": "Lorem ipsum",
        "second_cell_name": "dolor sit",
        "third_cell_name": "amet."
    }

    test_string = "Lorem ipsum dolor sit amet."
