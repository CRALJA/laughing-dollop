import csv
from pprint import pprint
import pymongo
from datetime import datetime, timedelta


date = datetime.strptime('2004-12-30', '%Y-%m-%d').date()
l1 = []
l2 = []
m = []

with open(r'C:\Users\Student\Documents\laughing-dollop\Data Sources\Self-Employment\Self-employment date along top.csv', 'r') as f:
    reader = csv.reader(f)
    for r in reader:
        if r[-1] not in ('') and r[4] != 'Conf':
            l1.append(r)

with open(r'C:\Users\Student\Documents\laughing-dollop\Data Sources\Employment\unemployment.csv', 'r') as f:
    reader = csv.reader(f)
    for r in reader:
        if len(r) > 20 and r[2] != 'Conf':
            l2.append(r)


for i in range(80):
    d = {}
    e = {}
    d['city'] = l1[i][0].split(':')[1]
    d['employment_rates'] = []
    for n in range(51):
        f = {}
        quarter = date + timedelta(days = 91*n)
        f['self_employed'] = l1[i][3 + n*4]
        f['unemployed'] = l2[i][1 + n*2]
        d['employment_rates'].append({str(datetime.strftime(quarter, '%Y-%m'))+'-01': f})
    m.append(d)

for j in m:
    pymongo.MongoClient("mongodb://localhost").uber.employment.insert(j)
