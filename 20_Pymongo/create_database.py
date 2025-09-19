import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db =client['mydb']
dblist = client.list_database_names()
if "mydb" in dblist:
    print("exist")
else:
    print("not Exist")