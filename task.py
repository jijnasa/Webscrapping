# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 16:31:29 2020

@author: Jijnasa
"""

from bs4 import BeautifulSoup
import dateutil.parser as parser
import requests
import csv
from collections import defaultdict
r = requests.get("https://en.wikipedia.org/wiki/2019_in_spaceflight#Orbital_launches")
soup = BeautifulSoup(r.content, "html.parser")
table = soup.find_all('table')[3]
rows = table.find_all('tr')
row_list = list()
for tr in rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    row_list.append(row)
d = defaultdict(lambda: 0)
for row in row_list[3:]:
    if(len(row)==5):
        date3 = row[0].split('(',1)[0]
        flag = False
        d[date3]=0
    if(len(row)==6 and flag == False):
        if(row[-1] == 'Operational\n' or row[-1] == 'En Route\n' or row[-1]=='Sucessful\n'):
            d[date3] += 1
            flag = True
    else:
        continue
#date2 = parser.parse("26 December23:11:57\r")
with open('result.csv', mode='w') as file:
    for x in d:
        date1 = x.split('[',1)[0]
        date2 = parser.parse(date1)
        print(date2.isoformat()+',',d[x])
        data_n = date2.isoformat()
        file.write(data_n+','+str(d[x]))
        file.write('\n')