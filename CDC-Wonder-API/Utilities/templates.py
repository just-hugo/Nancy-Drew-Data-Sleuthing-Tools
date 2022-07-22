from csv_utilities import find

class template:

    def __init__(self):
        return

    find = find()

    header_row = {'gender': 'Gender',
              'race': 'Race',
              'deaths': 'Number of Deaths',
              'year': 'Year',
              'pop': 'Population',
              'crude_rate': 'Crude Rate Per Capita'}

    def cells(self, each_row):

        cells = {'gender': find.cell(each_row, 'c[l]', 0, 'l'),
             'race': find.cell(each_row, 'c[l]', 1, 'l'),
             'year': find.cell(each_row, 'c[l]', 2, 'l'),
             'deaths': find.cell(each_row, 'c[v]', 0, 'v'),
             'pop': find.cell(each_row, 'c[v]', 1, 'v'),
             'crude_rate': find.cell(each_row, 'c[v]', 2, 'v')}
        print(cells['gender'])
        print('***')
        return print(cells['gender'])

