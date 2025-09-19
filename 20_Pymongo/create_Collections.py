import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['db']
myclo1 = db['my_collection']
listcollection = db.list_collection_names()

if "my_collection" in listcollection:
    print("Exist")
else:
    print("Not Exist")