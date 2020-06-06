from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

target = db.movie.find_one({'title':'매트릭스'})
target_rate = target['star']

db.movie.update_many({'star':target_rate},{'$set':{'star':0}})
