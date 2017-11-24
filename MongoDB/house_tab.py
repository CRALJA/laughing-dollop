""" code to load tableau ready house price data into Mongo. The files for this code are in the data sources file"""

import csv
from pprint import pprint
import pymongo
from datetime import datetime

# setting the empty lists and dictionaries which will be filled later
l = []
u = []
d = {}

def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month

# opening the Uber launch dates csv file, adding rows into a list
# this code also sets the date format to mmm-yy
with open(r'C:\Users\Student\Documents\laughing-dollop\Data Sources\Uk_cities_uber_deployment.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for r in reader:
        if r[1] == 'Y':
            a = []
            a.append(r[0])
            a.append(datetime.strptime(r[2], '%b-%y'))
            u.append(a)

# opening the house price data csv file, appending rows into a list
with open(r'C:\Users\Student\Documents\laughing-dollop\Data Sources\Housing\UK-HPI-full-file-2017-08.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for r in reader:
        for i in range(len(u)):
            if datetime.strptime(r[0], '%d/%m/%Y') > datetime.strptime('01/01/2010', '%d/%m/%Y') and r[1] in u[i][0]:
                p = {}
                p['date'] = str(datetime.strptime(r[0], '%d/%m/%Y').date())
                p['price'] = r[3]
                #pprint(diff_month(datetime.strptime(r[0], '%d/%m/%Y'), u[i][1]))
                if d.get('city', 'na') == r[1]:
                    if abs(diff_month(datetime.strptime(r[0], '%d/%m/%Y'), u[i][1])) <= 12:
                        d['prices'].append(p)
                else:
                    l.append(d)
                    d = {}
                    d['city'] = r[1]
                    d['prices'] = []
                    d['launch'] = str(u[i][1].date())
                    d['prices'].append(p)

for i in l:
    pymongo.MongoClient("mongodb://localhost").uber.house_tab.insert(i)
