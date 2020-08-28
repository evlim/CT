# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 14:20:49 2020

@author: Evan
"""

import requests
from bs4 import BeautifulSoup
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

for t in all_strong_tags:
    t.text
    
###all_sublist = [all_strong_tags[x:x+3] for x in range(0, len(all_strong_tags), 3)]
###print(all_sublist)
