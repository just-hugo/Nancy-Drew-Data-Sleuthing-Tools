# Program to send a request to the FBI Crime API and save the response as a JSON.

from FBIEndpoints import Endpoints
import requests
import json

# Initializing the Endpoints module
FBI = Endpoints()

# Setting up the API URL for the FBI
baseURL_FBI = FBI.baseURL
endpoint_FBI = FBI.VictimDemographic('homicide-offenses', 'sex')
api_key_FBI = '?api_key=D5g6BuQ3aL9JXlrj7WaTjuKPrYwsERbgme1bnsrB'
combinedURL_FBI = baseURL_FBI + endpoint_FBI + api_key_FBI

# Setting up the API URL for the BJS
baseURL_BJS = 'https://api.bjs.ojp.gov'
endpoint_BJS = '/2018'
# data_format is optional and should be sent at the end of the API call. Can be set to json, xml, or csv
data_format_BJS = '?format=json'
combinedURL_BJS = baseURL_BJS + endpoint_BJS + data_format_BJS

# Setting up the filename to save the API response as
fileExt = '.json'
fileName = endpoint_FBI.replace('/', '-') + fileExt

# Creating a file to write data
with open(fileName, 'w') as file:
    # Hitting the API and saving the response as an object
    response = requests.get(combinedURL_FBI)
    # Converting the response object to a JSON
    j = response.json()
    # Writing the JSON to the file with easy-to-read formatting
    file.write(json.dumps(j, sort_keys=True, indent=4))
