# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 14:20:49 2020

@author: Evan
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

url = "http://publicinterestlegal.org/county-list/"
response = requests.get(url, headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})
#if response.status_code == 200:
#    print("Success")
#else:
#    print("Failure")

results_page = BeautifulSoup(response.content,'lxml')
#print(results_page)

all_strong_tags = results_page.find_all('strong')[3:]

#print (all_strong_tags)

list=[] 
for t in all_strong_tags: 
    list.append(t.text)
#print(list)

#all_sublist = [list[x:x+3] for x in range(0, len(list), 3)]
#print(all_sublist)

lines = [list]
labels = ['COUNTY', 'STATE', 'REGISTRATION RATE']
df = pd.DataFrame(np.array(lines).reshape(141,3), columns = labels)
#print(df)
# Return 2d list
list_w_sub = df.values.tolist()
list_w_sub.insert(0, labels)
#print (list_w_sub)

print ("elim")
print (len(list_w_sub))
print (list_w_sub)