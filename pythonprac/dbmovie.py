from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://test:sparta@cluster0.0saih.mongodb.net/Cluster0?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.dbsparta


db.movies.update_one({'title':'가버나움'},{'$set':{'star':'0'}})

