import csv
from pprint import pprint
import pymongo
from datetime import datetime
import itertools

l2011 = []
l2013 = []
l2015 = []
l2017 = []

with open(r'C:\Users\Student\Documents\laughing-dollop\Data Sources\taxi\taxi2011.csv', 'r') as f:
    reader = csv.reader(f)
    for r in reader:
        if r[2] not in (''): # entries we want have the area name in the 2nd or 3rd entry of r
#this does however involve categories i.e Tyne and wear for gateshead etc.
            d = {}
            d['la_code'] = r[0]
            d['name'] = r[2]
            d['date'] = str(datetime.strptime('2011-03-31', '%Y-%m-%d').date())
            d['taxis'] = r[7]
            d['phv'] = r[11]
            d['total_dri'] = r[16]
            d['total_veh'] = r[17]
            l2011.append(d)
        if r[3] not in (''):
            d = {}
            d['la_code'] = r[0]
            d['name'] = r[3]
            d['date'] = str(datetime.strptime('2011-03-31', '%Y-%m-%d').date())
            d['taxis'] = r[7]
            d['phv'] = r[11]
            d['total_dri'] = r[16]
            d['total_veh'] = r[17]
            l2011.append(d)

with open(r'C:\Users\Student\Documents\laughing-dollop\Data Sources\taxi\taxi2013.csv', 'r') as f:
    reader = csv.reader(f)
    for r in reader:
        if r[2] not in (''): # entries we want have the area name in the 2nd or 3rd entry of r
#this does however involve categories i.e Tyne and wear for gateshead etc.
            d = {}
            d['la_code'] = r[0]
            d['name'] = r[2]
            d['date'] = str(datetime.strptime('2013-03-31', '%Y-%m-%d').date())
            d['taxis'] = r[7]
            d['phv'] = r[11]
            d['total_dri'] = r[16]
            d['total_veh'] = r[17]
            l2013.append(d)
        if r[3] not in (''):
            d = {}
            d['la_code'] = r[0]
            d['name'] = r[3]
            d['date'] = str(datetime.strptime('2013-03-31', '%Y-%m-%d').date())
            d['taxis'] = r[7]
            d['phv'] = r[11]
            d['total_dri'] = r[16]
            d['total_veh'] = r[17]
            l2013.append(d)

with open(r'C:\Users\Student\Documents\laughing-dollop\Data Sources\taxi\taxi2015.csv', 'r') as f:
    reader = csv.reader(f)
    for r in reader:
        if r[2] not in (''): # entries we want have the area name in the 2nd or 3rd entry of r
#this does however involve categories i.e Tyne and wear for gateshead etc.
            d = {}
            d['la_code'] = r[0]
            d['name'] = r[2]
            d['date'] = str(datetime.strptime('2015-03-31', '%Y-%m-%d').date())
            d['taxis'] = r[7]
            d['phv'] = r[11]
            d['total_dri'] = r[16]
            d['total_veh'] = r[17]
            l2015.append(d)
        if r[3] not in (''):
            d = {}
            d['la_code'] = r[0]
            d['name'] = r[3]
            d['date'] = str(datetime.strptime('2015-03-31', '%Y-%m-%d').date())
            d['taxis'] = r[7]
            d['phv'] = r[11]
            d['total_dri'] = r[16]
            d['total_veh'] = r[17]
            l2015.append(d)

with open(r'C:\Users\Student\Documents\laughing-dollop\Data Sources\taxi\taxi2017.csv', 'r') as f:
    reader = csv.reader(f)
    for r in reader:
        if r[2] not in (''): # entries we want have the area name in the 2nd or 3rd entry of r
#this does however involve categories i.e Tyne and wear for gateshead etc.
            d = {}
            d['la_code'] = r[0]
            d['name'] = r[2]
            d['date'] = str(datetime.strptime('2017-03-31', '%Y-%m-%d').date())
            d['taxis'] = r[7]
            d['phv'] = r[11]
            d['total_dri'] = r[16]
            d['total_veh'] = r[17]
            l2017.append(d)
        if r[3] not in (''):
            d = {}
            d['la_code'] = r[0]
            d['name'] = r[3]
            d['date'] = str(datetime.strptime('2017-03-31', '%Y-%m-%d').date())
            d['taxis'] = r[7]
            d['phv'] = r[11]
            d['total_dri'] = r[16]
            d['total_veh'] = r[17]
            l2017.append(d)

for i in itertools.chain(*[l2011, l2013, l2015, l2017]):
    pymongo.MongoClient("mongodb://localhost").uber.taxi.insert(i)

# for i in itertools.chain(*[l2011, l2013, l2015, l2017]):
#         pymongo.MongoClient("mongodb://localhost").uber.taxi.insert(i)
