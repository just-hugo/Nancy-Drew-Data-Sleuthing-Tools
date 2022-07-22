"""
Retrieves all homicides from the CDC Wonder API D140 database (Compressed Mortality, 1999-2016 Report).

Homicides are categorized by gender, race, and years 1999-2016.

CDC asks that automated queries get sent at least 2 minutes apart
"""

import requests

# API URL
baseURL = 'https://wonder.cdc.gov/controller/datarequest'
endpoint = '/D140'
combinedURL = baseURL + endpoint

# Response body file
fileExt = '.xml'
fileName = '../../API-Responses/' + endpoint.replace('/', '') + '_All_Homicides_By_Year' + fileExt

# Sends query parameters to the API and saves the response
with open(fileName, 'w') as file:
    with open('xml-string.txt', 'r') as parameters:
        # The API requires the POST request include the following data
        data = {'request_xml': parameters.read(), 'accept_datause_restrictions': 'true'}
        response = requests.post(combinedURL, data=data)
        file.write(response.text)

