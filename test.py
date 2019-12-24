import time
from pymongo import MongoClient

# MongoDB的客户端
client = MongoClient("localhost", 27017)
db = client['test']
# collection 相当于 table
gdb_collection = db['gdb']
user_log_collection = db['user_log']


def ins():
    res = gdb_collection.find_one()
    f1 = {
        'admin_id': 957360688,
        'admin_name': 'jdq',
        'el_id': res['_id'],
        'el_no': 'line0',
        'time': time.time(),
        # 'action': "%s_change_el_config:%s_%s" % (info["admin_name"], info["el_no"], changes)
        'action': "jdq_change_el_config: line0_el_no_el_url"
    }

    f7 = {
        'user_id': 347737909,
        'user_name': 'dobby',
        'time': time.time(),
        'action': "login_dobby"
    }

    result = user_log_collection.insert_one(f7)
    print(result.inserted_id)


# ins()
res = user_log_collection.find_one()

# res = user_log_collection.find_one({
#     'el_no': 'line0'
# })
print(res)
print(type(res['_id']))
print(res['_id'])
