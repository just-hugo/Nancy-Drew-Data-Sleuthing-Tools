# Program to send a request to the CDC Wonder API and save the response as an XML.

# CDC asks that automated queries get sent at least 2 minutes apart

import requests

# Setting up the API URL
baseURL = 'https://wonder.cdc.gov/controller/datarequest'
# Endpoint is the [database ID], preceded by a /
endpoint = '/D140'
combinedURL = baseURL + endpoint

# The CDC requires that a string in XML format be sent as a data parameter with a POST request to their API.

# This XML string contains query parameters to tell the server what information you want it to send back.

# Each branch of the XML tree is a set of parameters, grouped by type.

# Each group of parameters and each individual parameter is assigned a code which is used in the XML tree.

# There are two easy ways to locate these codes.
#
# 1. Header form data pulled from the network tab while using the user-facing query portal can be used as parameters

# 2. By navigating to the user-facing query portal and view its HTML source code.

# In the HTML, the JavaScript <name> for each text field will be set to the parameter's code.

# Each API has a slightly different set of parameters, but the XML structure remains the same.

# The XML structure is:

'''
<request-parameters>
    <parameter>
        <name>GROUP CODE</name>
        <value>PARAMETER CODE</value>
    </parameter>
    <parameter>
        <name>GROUP CODE</name>
        <value>PARAMETER CODE</value>
    </parameter>
</request-parameters>
'''
# Also: example request has <value/> on parameters with an empty value, instead of <value></value>.

# Setting up the filename to save the API response as
fileExt = '.xml'
fileName = endpoint.replace('/', '-') + fileExt

# Creating a file to write data
with open(fileName, 'w') as file:
    with open('header_data_xml_string.txt') as parameters:
        data = {'request_xml': parameters.read(), 'accept_datause_restrictions': 'true'}
        # Hitting the API and saving the response as an object
        response = requests.post(combinedURL, data=data)
        print(response)
        # Convert the data as necessary to save as a readable XML
        file.write(response.text)

# The response is an xml file. The results are located in the <data-field> tag.

# Each <c> tag is equivalent to a spreadsheet cell.
