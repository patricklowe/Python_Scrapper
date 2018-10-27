# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 14:05:33 2018
Guided by blog post: https://towardsdatascience.com/data-science-skills-web-scraping-using-python-d1a85ef607ed
Original by: Dr Kerry Parker
@author: Patrick Lowe
"""
# importing libraries
from bs4 import BeautifulSoup
import urllib.request
import csv

#   Specify the URL
urlpage =   'http://www.fasttrack.co.uk/league-tables/tech-track-100/league-table/'

#   Query the website and return the html to the variable 'page'
page = urllib.request.urlopen(urlpage)

#   Parse the HTML using BS and store in variable 'Soup'
soup = BeautifulSoup(page,'html.parser')

#   Print the results
#print(soup)

#   Create customer error handler
#--------------

#   Find results within the table
table = soup.find('table', attrs={'class': 'tableSorter'})
results = table.find_all('tr')
print('Number of results', len(results))

#   Create and write headers to a list 
rows = []
rows.append(['Rank', 'Company Name', 'Webpage', 'Description', 'Location', 'Year End', 'Annual Sales Rise over 3 Years', ' Sales $000s', 'Staff', 'Comments',])
#print(rows)

#   Loop over the results
for result in results:
#   Find all cloumns per result
    data = result.find_all('td')
#   Check that columns have data
    if len(data) == 0:
        continue
    
#   Write columsn to variables
    rank = data[0].getText()
    company = data[1].getText()
    location = data[2].getText()
    yearend = data[3].getText()
    salesrise = data[4].getText()
    sales = data[5].getText()
    staff = data[6].getText()
    comments = data[7].getText()
    print(rank)
#    extract description from the name
    companyname = data[1].find('span', attrs={'class':'company-name'}).getText()    
    description = company.replace(companyname, '')
    
#   remove unwanted characters
    sales = sales.strip('*').strip('†').replace(',','')

#    go to link and extract company website
    url = data[1].find('a').get('href')
    page = urllib.request.urlopen(url)
#    parse the html 
    soup = BeautifulSoup(page, 'html.parser')
#    find the last result in the table and get the link
    try:
        tableRow = soup.find('table').find_all('tr')[-1]
        webpage = tableRow.find('a').get('href')
    except:
            webpage = None

#    write each result to rows
    rows.append([rank, companyname, webpage, description, location, yearend, salesrise, sales, staff, comments])
#print(rows)

#    Create csv and write rows to output file
with open('techtrack100.csv','w', newline='') as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerows(rows)
