import csv
from pprint import pprint
import pymongo
from datetime import datetime, timedelta


bdate = datetime.strptime('2004-12-30', '%Y-%m-%d').date()
se = []
ue = []
e = []
l = []
u = []

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

with open(r'C:\Users\Student\Documents\laughing-dollop\Data Sources\Self-Employment\Self-employment date along top.csv', 'r') as f:
    reader = csv.reader(f)
    for r in reader:
        if r[-1] not in ('') and r[4] != 'Conf' and r[0].split(':')[1] != 'City of London': # remove city of london entry as this mainly consists of ! and -
            se.append(r)

with open(r'C:\Users\Student\Documents\laughing-dollop\Data Sources\Employment\unemployment.csv', 'r') as f:
    reader = csv.reader(f)
    for r in reader:
        if len(r) > 20 and r[2] != 'Conf' and r[0] != 'City of London':
            ue.append(r)

for i in range(79):
    for j in range(len(u)):
        if se[i][0].split(':')[1] in u[j][0]:
            d = {}
            d['city'] = se[i][0].split(':')[1]
            d['launch'] = str(u[j][1].date())
            d['employment_rates'] = []
            for n in range(51):
                f = {}
                quarter = bdate + timedelta(days = 91*n)
                if d.get('city', 'nope') == ue[i][0]:
                    f['self_employed'] = float(se[i][3 + n*4])
                    f['unemployed'] = float(ue[i][1 + n*2])
                    f['date'] = str(datetime.strftime(quarter, '%Y-%m'))+'-01'
                if abs(diff_month(datetime.strptime(f['date'], '%Y-%m-%d'), u[j][1])) <= 12:
                    d['employment_rates'].append(f)
            e.append(d)

for j in e:
    pymongo.MongoClient("mongodb://localhost").uber.employment_tab.insert(j)
