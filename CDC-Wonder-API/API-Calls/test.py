import requests
from bs4 import BeautifulSoup
from selenium import webdriver

cookies = ['s_fid=64A0EC0CD243D41A-1D970094C5722F56',
            's_cc=true',
            's_vnum=1609480800047%26vn%3D30',
            's_invisit=true',
            's_lv_s=Less%20than%201%20day',
            's_visit=1', 'TS0121a97c=015d0abe874c34e2aac7859260905290463fda37b5af3c2b16a71b906c58e4578604dcb064c67ae38e854506f616961fc1a203cfbe35133e06fa85ae6d9bead9d666373840',
           'gpv_v45=Compressed%20Mortality%2C%201999-2016%20Request',
           'gpv_c54=https%3A%2F%2Fwonder.cdc.gov%2Fcmf-icd10.html%3Fstage%3Dabout%26saved_id%3D%26action-I%2BAgree%3DI%2BAgree',
           's_ppvl=Compressed%2520Mortality%252C%25201999-2016%2520Request%2C21%2C100%2C1891%2C763%2C394%2C1440%2C900%2C2%2CL',
           's_pvs=%5B%5BB%5D%5D',
           's_tps=%5B%5BB%5D%5D',
           's_ptc=0.01%5E%5E0.00%5E%5E0.00%5E%5E0.00%5E%5E0.24%5E%5E0.95%5E%5E1.54%5E%5E0.01%5E%5E1.97',
           's_ppv=Compressed%2520Mortality%252C%25201999-2016%2520Request%2C21%2C74%2C1394%2C763%2C394%2C1440%2C900%2C2%2CL',
           's_lv=1607738257822',
           's_sq=devcdc%3D%2526c.%2526a.%2526activitymap.%2526page%253DCompressed%252520Mortality%25252C%2525201999-2016%252520Request%2526link%253DClick%252520the%252520I%252520Agree%252520button%252520to%252520gain%252520access%252520to%252520the%252520dataset%252520and%252520signify%252520that%252520you%252520will%252520abide%252520by%252520the%252520terms%252520of%252520the%252520data%252520use%252520agreement.%2526region%253Dwonderform%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c%2526pid%253DCompressed%252520Mortality%25252C%2525201999-2016%252520Request%2526pidt%253D1%2526oid%253Dfunctiononclick%252528event%252529%25257BsendTab%252528%252529%25257D%2526oidt%253D2%2526ot%253DSUBMIT']

xml_string = '''<query-parameters>
<parameter>
<name>stage</name>
<value>about</value>
</parameter>
<parameter>
<name>saved_id</name>
<value></value>
</parameter>
<parameter>
<name>action-I Agree</name>
<value>I Agree</value>
</parameter>
<parameter>
<name>O_icd</name>
<value></value>
</parameter>
</query-parameters>
'''

data = {'request_xml': xml_string}

response = requests.post('https://wonder.cdc.gov/controller/datarequest/D76', data=data, cookies=cookies)
print(response.text)
print(response)
