import csv
from pprint import pprint
import pymongo


l = []
m = []

with open(r'C:\Users\Student\Documents\laughing-dollop\Data Sources\Population\population.csv', 'r') as f:
    reader = csv.reader(f)
    for r in reader:
        l.append(r)

for i in l[9:-18]:
    d = {}
    rates = {}
    d['city'] = i[0].split(':')[1]
    rates['16-64(%)'] = i[11]
    rates['16-19(%)'] = i[31]
    rates['20-24(%)'] = i[35]
    rates['25-34(%)'] = i[39]
    rates['35-49(%)'] = i[43]
    rates['50-64(%)'] = i[47]
    rates['60+(%)'] = i[51]
    d['total'] = i[2]
    d['rate'] = rates
    m.append(d)

for j in m:
    pymongo.MongoClient("mongodb://localhost").uber.population.insert(j)
