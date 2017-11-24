import csv
from pprint import pprint
import pymongo
from datetime import datetime


l = []
u = []
d = {}

def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month

with open(r'C:\Users\Student\Documents\laughing-dollop\Data Sources\Uk_cities_uber_deployment.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for r in reader:
        if r[1] == 'Y':
            a = []
            a.append(r[0])
            a.append(datetime.strptime(r[2], '%b-%y'))
            u.append(a)

with open(r'C:\Users\Student\Documents\laughing-dollop\Data Sources\Crime\crime(filtered).csv', 'r') as f:
    reader = csv.reader(f)
    for r in reader:
        for i in range(len(u)):
            if r[1][:-5] in u[i][0]:
                c = {}
                c['date'] = str(datetime.strptime(r[0], '%Y-%m').date())
                c['crime_type'] = r[-2]
                c['outcome'] = r[-1]
                if d.get('city', 'na') == u[i][0]:
                    if abs(diff_month(datetime.strptime(r[0], '%Y-%m'), u[i][1])) <= 12:
                        d['crimes'].append(c)
                else:
                    d = {}
                    d['city'] = u[i][0]
                    d['lsoa'] = r[2]
                    d['launch'] = str(u[i][1].date())
                    d['crimes'] = []
                    l.append(d)

for i in l:
    pymongo.MongoClient("mongodb://localhost").uber.crime_tab.insert(i)
