from bs4 import BeautifulSoup
from csv_utilities import make, find, Add, read
from templates import template

# TODO: refactor below to use approach #3 in https://medium.com/swlh/how-can-we-best-switch-in-python-458fb33f7835

make = make()
find = find()
add = Add()
read = read()
template = template()

# Combined total homicides for all demographics, genders, and years.
combined_totals_table = make.new_table(
    template.header_row['deaths'],
    template.header_row['pop'],
    template.header_row['crude_rate'])

# Total homicides for each gender and race for all years.
demographic_totals_table = make.new_table(
    template.header_row['gender'],
    template.header_row['race'],
    template.header_row['deaths'],
    template.header_row['pop'],
    template.header_row['crude_rate'])

# Homicides for all years by gender.
gender_totals_table = make.new_table(
    template.header_row['gender'],
    template.header_row['deaths'],
    template.header_row['pop'],
    template.header_row['crude_rate'])

# Homicides for each gender and race for each year.
year_by_year_table = make.new_table(
     template.header_row['gender'],
     template.header_row['race'],
     template.header_row['year'],
     template.header_row['deaths'],
     template.header_row['pop'],
     template.header_row['crude_rate'])

# Transform API response file into a syntax tree
api_data = make.xml_tree(read.file('../API-Responses/D140_All_Homicides_By_Year.xml'))

# Search the tree for the table generated by the query parameters
data_table = find.cell(api_data, 'r')

for each_row in data_table:

    # Finding the rows with totals
    a_total_row = find.cell(each_row, 'c[dt]')

    # Finding the rows for homicides per year
    a_year_row = find.cell(each_row, 'c[v]')

    # Year by year gender and race homicide rates
    if a_year_row:

        cells = {'gender': find.cell(each_row, 'c[l]', 0, 'l'),
             'race': find.cell(each_row, 'c[l]', 1, 'l'),
             'year': find.cell(each_row, 'c[l]', 2, 'l'),
             'deaths': find.cell(each_row, 'c[v]', 0, 'v'),
             'pop': find.cell(each_row, 'c[v]', 1, 'v'),
             'crude_rate': find.cell(each_row, 'c[v]', 2, 'v')}

        year_by_year_row = add.cells_to_row(cells)

        add.row_to_table(year_by_year_row, year_by_year_table)

    # Total homicides by Demographic (race and gender) Gender, and combined
    elif a_total_row:

        # Demographic (Race and Gender) totals
        if len(each_row) == 6:

            cells = {'gender': find.cell(each_row, 'c[l]', 0, 'l'),
                     'race': find.cell(each_row, 'c[l]', 1, 'l'),
                     'deaths': find.cell(each_row, 'c[dt]', 0, 'dt'),
                     'pop': find.cell(each_row, 'c[dt]', 1, 'dt'),
                     'crude_rate': find.cell(each_row, 'c[dt]', 2, 'dt')}

            demographic_totals_row = add.cells_to_row(cells)

            add.row_to_table(demographic_totals_row, demographic_totals_table)

        # Gender totals
        elif len(each_row) == 5:

            cells = {'gender': find.cell(each_row, 'c[l]', 0, 'l'),
                     'deaths': find.cell(each_row, 'c[dt]', 0, 'dt'),
                     'pop': find.cell(each_row, 'c[dt]', 1, 'dt'),
                     'crude_rate': find.cell(each_row, 'c[dt]', 2, 'dt')}

            gender_totals_row = add.cells_to_row(cells)

            add.row_to_table(gender_totals_row, gender_totals_table)

        # Combined totals
        else:

            cells = {'deaths': find.cell(each_row, 'c[dt]', 0, 'dt'),
                     'pop': find.cell(each_row, 'c[dt]', 1, 'dt'),
                     'crude_rate': find.cell(each_row, 'c[dt]', 2, 'dt')}

            combined_total_row = add.cells_to_row(cells)

            add.row_to_table(combined_total_row, combined_totals_table)

make.csv_file('D140_year_by_year.csv', year_by_year_table)

make.csv_file('D140_demographic_totals.csv', demographic_totals_table)

make.csv_file('D140_combined_totals.csv', combined_totals_table)

make.csv_file('D140_gender_totals.csv', gender_totals_table)
