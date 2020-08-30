  
# -*- coding: utf-8 -*-

import requests
from lxml import etree

url = "http://www.ncdc.noaa.gov/cag/statewide/rankings/44-tavg-201608/data.xml"
response = requests.get(url).content

root = etree.XML(response)


print("elim")
print(root[3+4][1].text)
print(root[3+4][2].text)
print(root[3+4][3].text)
print(root[3+4][4].text)
print(root[3+4][5].text)
#for element in root.iter("value"):
#    print(element.tag)
#for element in root.iter("data"):
#    print (element.find("value").text)
    