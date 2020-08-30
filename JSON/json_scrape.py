# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 16:40:41 2020

@author: Evan
"""

import requests
url = "https://buckets.peterbeshai.com/api/?player=201939&season=2015"
response = requests.get(url, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"})
#response = requests.get(url)
#print (str((response.json())))
    
"""
#This result is not correct 

list_action = []
for shot in response.json():
    list_action.append(shot["ACTION_TYPE"])

jump_shot = 0    
for i in list_action:
    if i.count("Jump Shot") == 1:
        jump_shot += 1

#Cause tho case sensitive, will count things like below

string = "Fadeaway Jump Shot"
string.count("Jump Shot") == 1 #true
"""

num_jump_shot = str((response.json())).count("""'Jump Shot'""")
num_made_jump_shot = str((response.json())).count("""'Made Shot', 'ACTION_TYPE': 'Jump Shot'""")    
percentage_jump_shot = str("{:.1f}".format(num_made_jump_shot / num_jump_shot * 100)) +"%"

print ("elim")
print (num_jump_shot)
print (num_made_jump_shot)
print (percentage_jump_shot)