import json
import ast

file = 'NIBR-Homicide-Victim-National-Count-API-Call.json'

with open(file) as file:
    parsed1 = json.load(file)
    #parsed2 = ast.literal_eval(file.read())
    #parsed3 = json.loads(file.read())
    #print('*** BEGINNING PARSED_JSON***' + parsed_json + '*** COMPLETE WITH PARSED_JSON ***')
    print(parsed1['data'][1]['data_year'])
    for item in parsed1['data'][1][x]:
        if x == 'data_year':
            print('data_year')
        elif x != 'data_year':
            continue