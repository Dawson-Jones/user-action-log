from pymongo import MongoClient

# MongoDB的客户端
client = MongoClient('mongodb://root:123456@192.168.1.7:27017')
db = client['tttt']
# collection 相当于 table
user_log_collection = db['user_log']

