import csv
from bs4 import BeautifulSoup


class Error:

    def __init__(self):
        return

    def invalid_input(self, argument, expected_argument_types):
        """
        argument is whatever argument was used in the initial function.

        expected_argument_types is a list of strings of the data types the argument could be.
        """

        actual_argument_type = type(argument)

        if expected_argument_types.__contains__(actual_argument_type):
            return

        elif expected_argument_types.__contains__(actual_argument_type) is False:
            raise TypeError(
                f"Cell argument cannot be a {actual_argument_type}. Valid cell types are: {expected_argument_types}")

        else:
            raise BaseException

class Add:

    def __init__(self):
        return

    def cell_to_row(self, cell: str, row_name: list) -> list:
        """
        Pass a string as the first argument to add a single cell to a spreadsheet row.

        Pass a list as the first argument to add an entire row of cells to a spreadsheet.

        The row_name argument is a list that represents a row of a spreadsheet; each entry in the list is a cell in the row.

        The list can be empty or partially populated. If empty, the cell will become the first entry in the row.

        If the row list is already populated, the cell argument will be appended to the end of the list.

        This will appear on the spreadsheet as though the already-populated row has been expanded by one cell.
        """

        if type(cell) is str or type(cell) is list:
            row_name.append(cell)
            return row_name

        else:
            Error().invalid_input(cell, [str, list])

    def cells_to_row(self, cell_selectors: dict, *args: list) -> list:
        """
        **Functions**

        add.cells_to_row_by_selector() has one mandatory argument and one optional argument.

         The mandatory argument is a dictionary of one or more cells and their data.

        For example:

        {"cell_name": "cell data"}

        The second, optional, argument is a list, empty or populated with entries.

        The list represents a spreadsheet row. Each list entry is a cell.

        If the optional list argument is included, then each entry in the dictionary will be added to the list.

        Then it will return a list containing string  data for each cell.

        **Usage**

        The returned list can be added to a spreadsheet as a row by using it as the first argument in add.row_to_table().

        The cell data can be in the form of a cell selector built using find.cell() to pull data from a beautifulsoup4 object.
        """

        if args:
            if not isinstance(*args, list):
                Error().invalid_input(*args)

            row_of_cells = args[0]

            for cell_entry in cell_selectors:

                row_of_cells.append(cell_selectors[cell_entry])

            return row_of_cells

        elif len(args) == 0:
            if not isinstance(cell_selectors, dict):
                Error().invalid_input(cell_selectors, [dict])

            row_of_cells = []

            for cell_entry in cell_selectors:

                row_of_cells.append(cell_selectors[cell_entry])

            return row_of_cells

    def row_to_table(self, row_to_add, table_list):
        return table_list.append(row_to_add)


class find:

    def __init__(self):
        return

    def cell(self, soup_object, x=str, y=None, z=None):
        """
        Row must be a BeautifulSoup object.

        x is a string, y is a number, z is a string. These are positional coordinates for the Beautiful Soup syntax tree.

        Arguments must be submitted in one of the following combinations: (row, x) or (row, x, y, z).

        (row, x, y) and (row x, z) are not permitted.
        """

        if z:
            return soup_object.select(x)[y][z]
        elif z is None:
            if y is None:
                return soup_object.select(x)
            else:
                raise Exception()


class make:

    def __init__(self):
        return

    def csv_file(self, csv_file_name, csv_data):
        # csv_data should be a list of lists, where each list is a row and each item is a cell, ex [[Row, 1][Row, 2]]
        with open(csv_file_name, mode='w', newline='') as file:
            write = csv.writer(file)
            write.writerows(csv_data)
        return print(csv_file_name + ' has been made.')

    def new_table(self, *args):
        test = []
        for arg in args:
            test.append(arg)
        return [test]

    def xml_tree(self, response_file):
        return BeautifulSoup(response_file, "html.parser")


class read:

    def __init__(self):
        return

    def file(self, filename):
        with open(filename, 'r') as file:
            return file.read()

    def table_data(self, data_table):
        year_by_year_table = []
        for each_row in data_table:
            try:
                cells = {'gender': find.cell(self, each_row, 'c[l]', 0, 'l'),
                         'race': find.cell(self, each_row, 'c[l]', 1, 'l'),
                         'year': find.cell(self, each_row, 'c[l]', 2, 'l'),
                         'deaths': find.cell(self, each_row, 'c[v]', 0, 'v'),
                         'pop': find.cell(self, each_row, 'c[v]', 1, 'v'),
                         'crude_rate': find.cell(self, each_row, 'c[v]', 2, 'v')}

                year_by_year_row = add.cells_to_row(self, cells)
                add.row_to_table(self, year_by_year_row, year_by_year_table)
                print(year_by_year_row)
            except:
                print('except')
        return
