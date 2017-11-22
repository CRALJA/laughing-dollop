import csv
from pprint import pprint
import pymongo
from datetime import datetime
import itertools
import time

l = []
d = {}

for i in range(1, 8, 2):
    with open(r'C:\Users\Student\Documents\laughing-dollop\Data Sources\taxi\taxi201'+str(i)+r'.csv', 'r') as f:
        reader = csv.reader(f)
        for r in reader:
            if r[2] not in (''):# entries we want have the area name in the 2nd or 3rd entry
#this does however involve categories i.e Tyne and wear for gateshead etc.
                data = {}
                data['date'] = str(datetime.strptime('201'+str(i)+'-03-31', '%Y-%m-%d').date())
                data['taxis'] = int(r[7].replace(',', ''))
                data['phv'] = int(r[11].replace(',', ''))
                data['total_dri'] = int(r[-2].replace(',', ''))
                data['total_veh'] = int(r[-1].replace(',', ''))
                new_city = True
                for n in range(len(l)):
                    if l[n].get('city', 'na') == r[2]:
                        l[n]['data'].append(data)
                        new_city = False
                if new_city == True:
                    d = {}
                    d['la_code'] = r[0]
                    d['city'] = r[2]
                    d['data'] = []
                    d['data'].append(data)
                    l.append(d)
            if r[3] not in (''):
                data = {}
                data['date'] = str(datetime.strptime('201'+str(i)+'-03-31', '%Y-%m-%d').date())
                data['taxis'] = int(r[7].replace(',', ''))
                data['phv'] = int(r[11].replace(',', ''))
                data['total_dri'] = int(r[-2].replace(',', ''))
                data['total_veh'] = int(r[-1].replace(',', ''))
                new_city = True
                for n in range(len(l)):
                    if l[n].get('city', 'na') == r[3]:
                        l[n]['data'].append(data)
                        new_city = False
                if new_city == True:
                    d = {}
                    d['la_code'] = r[0]
                    d['city'] = r[3]
                    d['data'] = []
                    d['data'].append(data)
                    l.append(d)

for i in l:
    pymongo.MongoClient("mongodb://localhost").uber.taxi.insert(i)
