import pymongo

client=pymongo.MongoClient("mongodb+srv://ravikashyap760:RsplnS93qdRBRPr5@cluster0.tvarvtu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db=client.test
print(db)

d={
    "name":"RAVI",
    "email":"ravi1@gmail.com",
    "surname": "KASHYAP"
}
db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)
