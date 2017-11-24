import csv
from pprint import pprint
import pymongo
from datetime import datetime
import itertools
import time


#create empty list and dictionary
l = []
d = {}


#opens multiple csv's, taxi2011, taxi2013, taxi2015 and taxi 2017, one after the other
for i in range(1, 8, 2):
    with open(r'C:\Users\Student\Documents\laughing-dollop\Data Sources\taxi\taxi201'+str(i)+r'.csv', 'r') as f:
        reader = csv.reader(f)
        for r in reader:
            for j in range(2, 4):
                if r[j] not in (''):# entries we want have the area name in the 2nd or 3rd entry
    #this does however involve categories i.e Tyne and wear for gateshead etc.
                    data = {} #create empty dictionary each time and assign values after
                    data['date'] = str(datetime.strptime('201'+str(i)+'-03-31', '%Y-%m-%d').date()) #create date string i.e '2011-03-31'
                    data['taxis'] = int(r[7].replace(',', '')) #remove commas and set to int type
                    data['phv'] = int(r[11].replace(',', ''))
                    data['total_dri'] = int(r[-2].replace(',', ''))
                    data['total_veh'] = int(r[-1].replace(',', ''))
                    new_city = True #set new_city to true
                    for n in range(len(l)):
                        if l[n].get('city', 'na') == r[j]: #if the city name already exists the set new_city to false
                            l[n]['data'].append(data)
                            new_city = False
                    if new_city == True: #if new_city is true then create new dictionary and assign values
                        d = {}
                        d['la_code'] = r[0]
                        d['city'] = r[j]
                        d['data'] = []
                        d['data'].append(data)
                        l.append(d)

#load into mongodb in the database uber with the collection name 'taxi'
for k in l:
    pymongo.MongoClient("mongodb://localhost").uber.taxi.insert(k)
