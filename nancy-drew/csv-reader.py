import csv

offenseCount = 'NIBR-Homicide-Offense-National-Count-API-Call.txt'

with open('NIBR-Homicide-Offense-National-Count-API-Call.txt') as file:
    csv_reader = csv.reader(file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print('Done')

