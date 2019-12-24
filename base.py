from pymongo import MongoClient

# MongoDB的客户端
client = MongoClient("localhost", 27017)
db = client['test']
# collection 相当于 table
user_log_collection = db['user_log']

