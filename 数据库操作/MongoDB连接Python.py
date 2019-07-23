from pymongo import MongoClient
from bson.objectid import ObjectId #用于id查询

#连接服务器
conn=MongoClient("localhost",27017)

# 连接数据库
db = conn.mydb

# 获取集合
collection = db.student

# 添加文档,插入一条
collection.insert({'name:abc,'age:30''})

# 添加文档,插入多条
collection.insert([{'name:abc,'age:30''},{'name:xzl,'age:31''}])

conn.close()


'''
查询操作，注意：要加双引号,返回的结果是一个字典
'''
res = collection.fin({"age":{"$gt":18}})
for row in res:
    print(row)
'''
根据ID查询
'''
res = collection.fin({"_id":ObjectId("?")})
print(res[?])
