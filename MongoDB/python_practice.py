import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']

mycol = mydb['costomers']

# mydict = { "name": "John", "address": "Highway 40" }
#
# mydoc = mycol.insert_one(mydict)

# print(mydb.list_collection_names())
# print(myclient.list_database_names())
# for i in mycol.find():
#     print(i)

myquery = { "address": "Highway 40" }

for x in mycol.find():
  print(x)