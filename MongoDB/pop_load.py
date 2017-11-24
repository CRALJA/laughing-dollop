import csv
from pprint import pprint
import pymongo


#Create emply lists to append later
l = []
m = []

#open population csv and append each row that isn't the header row, does not have '' in the last entry and are not for the City of London into the list l. This produces a list of lists.
with open(r'C:\Users\Student\Documents\laughing-dollop\Data Sources\Population\population.csv', 'r') as f:
    reader = csv.reader(f)
    for r in reader:
        if r[-1] not in ('') and r[4] != 'Conf' and r[0].split(':')[1] != 'City of London':
            l.append(r)

#for each entry in l create a new dictionary and assign to each section of the dictionary then append to the list m.
for i in l:
    d = {}
    d['city'] = i[0].split(':')[1] #split the first element in the list then take the second part, producing just the city name
    d['rates'] = []
    d['rates'].append({'range': '16-64(%)', 'rate': float(i[11])})
    d['rates'].append({'range': '16-19(%)', 'rate': float(i[31])})
    d['rates'].append({'range': '20-24(%)', 'rate': float(i[35])})
    d['rates'].append({'range': '25-34(%)', 'rate': float(i[39])})
    d['rates'].append({'range': '35-49(%)', 'rate': float(i[43])})
    d['rates'].append({'range': '50-64(%)', 'rate': float(i[47])})
    d['rates'].append({'range': '60+(%)', 'rate': float(i[51])})
    d['total'] = i[2]
    m.append(d)

#load into mongodb in database uber with the collection called 'population'
for j in m:
    pymongo.MongoClient("mongodb://localhost").uber.population.insert(j)
