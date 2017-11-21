import pyodbc
import json
import pymongo
from pprint import pprint

c = pyodbc.connect(r'DSN=MySQLConn;UID=python;PWD=password')
cur = c.cursor()

con = pymongo.MongoClient("mongodb://localhost")
db = con.kubrick
r = db.sales

#listitem = {}
#
#listofdicts = []
#
#newdict = {}
#
#basketvalue = []
#basketitems = {}

sql = """select
	 soh.SalesOrderNumber
	,sod.LineTotal
	,sod.OrderQty
	,p.firstname + ' ' + p.lastname customer
	,replace(pr.Name, ',', '') productname
	,ps.name productsubcategory
	,pc.name productcategory
from sales.salesorderheader soh
inner join sales.customer c
	 on soh.CustomerID = c.CustomerID
inner join person.person p
	 on c.PersonID = p.BusinessEntityID
inner join sales.SalesOrderDetail sod
	 on soh.SalesOrderID = sod.SalesOrderID
inner join Production.Product pr
	 on sod.ProductID = pr.ProductID
inner join production.ProductSubcategory ps
	 on pr.ProductSubcategoryID = ps.ProductSubcategoryID
inner join production.productcategory pc
	 on ps.ProductCategoryID = pc.ProductCategoryID"""

# sql = "select * from production.product"

#for line in cur.execute(sql):
#    listitem['SalesOrderNumber'] = line[0]
#    listitem['CustomerName'] = line[3]
#    basketitems['ProductName'] = line[4]
#   # #basketitems['ProductSubCategory'] = line[5]
#    #basketitems['ProductCategory'] = line[6]
#    basketvalue.append(basketitems)
#    listitem['Basket'] = basketvalue
#   # listitem['Basket'] = [listitem['Name'] = line[4], listitem['SubCategory'] = line[5], listitem['Category'] = line[6]]
#    listofdicts.append(listitem)

#pprint(listofdicts)
SalesOrderNumber = []
sql_data = cur.execute(sql)
for row in sql_data:
    if row[0] in SalesOrderNumber:
        next
    else:
        SalesOrderNumber.append(row[0])

sql_data_dict = {}

for i in SalesOrderNumber:
    sql_data_dict[i] = []

# sql_data = cur.execute(sql)

for row in sql_data:
    if row[0] in sql_data_dict:
        sql_data_dict[row[0]].append({'Line Total':row[1], 'Order Quantity':row[2],
                                         'Customer':row[3],'Product Name':row[4],'Prod SubCat':row[5],'ProCat':row[6]})
    else:
        next
pprint(sql_data_dict)

#with open('sales.json', 'w') as s:
    #json.dump(sql_data_dict, s)