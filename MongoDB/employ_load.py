# code to load employment data into Mongo -- no adjustments made

import csv
from pprint import pprint
import pymongo
from datetime import datetime, timedelta

# bdate is available set to the first date in the dataset - it will be used later to calculate yearly quarters
bdate = datetime.strptime('2004-12-30', '%Y-%m-%d').date()
se = []
ue = []
e = []
l = []

# opening the self-employment csv file, adding rows into a list
with open(r'C:\Users\Student\Documents\laughing-dollop\Data Sources\Self-Employment\Self-employment date along top.csv', 'r') as f:
    reader = csv.reader(f)
    for r in reader:
        if r[-1] not in ('') and r[4] != 'Conf' and r[0].split(':')[1] != 'City of London':  # remove city of london entry as this mainly consists of ! and -
            se.append(r)

# opening the unemployment csv file, adding rows into a list
with open(r'C:\Users\Student\Documents\laughing-dollop\Data Sources\Employment\unemployment.csv', 'r') as f:
    reader = csv.reader(f)
    for r in reader:
        if len(r) > 20 and r[2] != 'Conf' and r[0] != 'City of London':
            ue.append(r)

# creating a dictionary with each city and the matching employment rates with dates as a list of dictionaries
for i in range(79):
    d = {}
    d['city'] = se[i][0].split(':')[1]
    d['employment_rates'] = []
    for n in range(51):
        f = {}
        quarter = bdate + timedelta(days = 91*n)
        if d.get('city', 'nope') == ue[i][0]:
            f['self_employed'] = float(se[i][3 + n*4])
            f['unemployed'] = float(ue[i][1 + n*2])
            f['date'] = str(datetime.strftime(quarter, '%Y-%m'))+'-01'
        d['employment_rates'].append(f)
    e.append(d)

#add dictionary to Mongo data base, db = uber, collection = employment
for j in e:
    pymongo.MongoClient("mongodb://localhost").uber.employment.insert(j)


# the following code will add the London dataset if needed
with open(r'C:\Users\Student\Documents\Uber\london.txt', 'r') as london:
    for k in london:
        if k != '\n':
            l.append(k[:-2])

p = [{"$match": {"city": {"$in": l}}}, {"$unwind": "$employment_rates"}, {"$group": {"_id": "$employment_rates.date", "unemployed": {"$avg": "$employment_rates.unemployed"}, "self_employed": {"$avg": "$employment_rates.self_employed"}}}, {"$sort": {"_id": -1}}]

lon = {}
lon['city'] = 'London'
lon['employment_rates'] = []
er = {}

for a in pymongo.MongoClient("mongodb://localhost").uber.employment.aggregate(pipeline = p):
    er["date"] = a["_id"]
    er["unemployed"] = a["unemployed"]
    er["self_employed"] = a["self_employed"]
    lon['employment_rates'].append(er)

pymongo.MongoClient("mongodb://localhost").uber.employment.insert(lon)
