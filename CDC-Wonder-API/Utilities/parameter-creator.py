"""
Takes raw header form data from the CDC Wonder query portal and formats it as an xml string.

To use, go to https://wonder.cdc.gov/controller/datarequest/D140 (or replace D140). Agree to their terms.

Fill out the query form with the parameters you want. CTRL + Right Click anywhere on the page, and select "Inspect".

In the developer tools menu, select the Network tab.

Click Send on the query form.

The page will load with your results. In the Network tab, find the request that begins with D140.

The request header will have a section called Form Data. Copy and paste this section into header_form_data.txt.

The file generated at the end of the script can be used in the POST call as parameters for CDC Wonder API.
"""

import re

with open('header-form-data.txt', 'r') as data:

    form_data_list = re.split("\n", data.read())
    parameter_list = []

    for x in form_data_list:

        parameter = re.split(":", x)
        parameter_list.append(parameter)

xml_tag = ['<name> </name>',
           '<value> </value>',
           '<parameter>',
           '</parameter>',
           '<request-parameters>',
           '</request-parameters>']

with open('../Query-Parameters/' + 'xml-string.txt', 'w') as xml_string:

    xml_string.write(xml_tag[4] + "\n")

    for x in parameter_list:

        parameter_name = re.sub(r"\s", x[0], xml_tag[0])
        parameter_value = re.sub(r"\s", x[1], xml_tag[1])

        xml_string.write(xml_tag[2] + "\n")
        xml_string.write(parameter_name + "\n")
        xml_string.write(parameter_value + "\n")
        xml_string.write(xml_tag[3] + "\n")

    xml_string.write(xml_tag[5])

'''
# Pseudocode -> code 

formData = 'header: blah'

print(re.split(":\s", formData))

keyValuePair = re.split(":\s", formData)

nameParam = re.sub("\s", keyValuePair[0], xmlTag[0])

print(nameParam)

valueParam = re.sub("\s", keyValuePair[1], xmlTag[1])

print(valueParam)
'''

'''
Pseudocode

<name></name>

formdata: blah 

take formdata from formdata: blah

insert formdata between <name> and </name>

take blah from formdata: blah

insert blah between <value> amd </value>
'''
