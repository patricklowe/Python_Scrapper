# -*- coding: utf-8 -*-
"""
Created on Fri Nov 09 18:14:33 2018
Guided by blog post: https://towardsdatascience.com/data-science-skills-web-scraping-using-python-d1a85ef607ed
Original by: Dr Kerry Parker
@author: Patrick Lowe
"""
# importing libraries
from bs4 import BeautifulSoup
import urllib.request
import csv

#   Specify the URL
urlpage =   "https://worldofwarcraft.com/en-gb/game/pve/leaderboards/hellfire/ataldazar"

#   Query the website and return the html to the variable "page"
page = urllib.request.urlopen(urlpage)

#   Parse the HTML using BS and store in variable "Soup"
soup = BeautifulSoup(page,"html.parser")

#   Print the results
#print(soup)

#   Create customer error handler
#--------------

#   Find results within the table
table = soup.find("div", attrs={"class": "SortTable-body"})
results = table.find_all("div", attrs={"class": "SortTable-row"})
#   Create and write headers to a list 
rows = []
rows.append(["Rank", "Mythic Level", "Time", "Tank","Tank Class", "Tank Profile", "Healer", "Healer Class", "Healer Profile", "DPS1", "DPS1 Class", "DPS1 Profile", "DPS2", "DPS2 Class", "DPS2 Profile", "DPS3", "DPS3 Class","DPS3 Profile"])

#   Loop over the results
for result in results:
    data = result.find_all("div")
    rank = data[0].text
    level = data[1].text
    time = data[2].text
    tank = data[3].find('div', attrs={'class':'List-item gutter-tiny'}).getText()
    tank_link = data[3].find('a')['href']
    tank_class = data[3].findAll('a')[0].attrs['class'][2][11:]

    healer = data[3].find_all('div', attrs={'class':'Character-name'})[1].text
    healer_link = data[3].findAll('a')[1].attrs['href']
    healer_class = data[3].findAll('a')[1].attrs['class'][2][11:]

    dps1 = data[3].find_all('div', attrs={'class':'Character-name'})[2].text
    dps1_link = data[3].findAll('a')[2].attrs['href']
    dps1_class = data[3].findAll('a')[2].attrs['class'][2][11:]
    
    dps2 = data[3].find_all('div', attrs={'class':'Character-name'})[3].text
    dps2_link = data[3].findAll('a')[3].attrs['href']
    dps2_class = data[3].findAll('a')[3].attrs['class'][2][11:]

    dps3 = data[3].find_all('div', attrs={'class':'Character-name'})[4].text
    dps3_link = data[3].findAll('a')[4].attrs['href']
    dps3_class = data[3].findAll('a')[1].attrs['class'][2][11:]
    
#    write each result to rows
    rows.append([rank, level, time, tank, tank_class, tank_link, healer, healer_class, healer_link, dps1, dps1_class, dps1_link, dps2, dps2_class, dps2_link, dps3, dps3_class, dps3_link])
#    Create csv and write rows to output file
with open('test.csv','w', encoding="utf-8",newline='') as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerows(rows)
    