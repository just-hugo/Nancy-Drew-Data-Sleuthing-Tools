from csv_utilities import make, Add, find, read
from bs4 import BeautifulSoup

soup = BeautifulSoup()
add = Add()
row = []

new_row = add.cell_to_row(9, row)

print(new_row)

"""read = read()
make = make()
add = add()
find = find()
soup = BeautifulSoup()

spreadsheet_list = []

header_row = ["Gender", "Murder Rate", "Race", "Age"]

spreadsheet_list.append(header_row)

print(spreadsheet_list)

data_row_1 = ["Female", "9", "White", "21"]

spreadsheet_list.append(data_row_1)

print(spreadsheet_list[1][2])"""
