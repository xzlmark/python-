from  pymongo  import MongoClient
from bson.objectid import ObjectId # 进行ID查询需要使用



#  未完成





class XzlMongDB:
    def __init__(self,db, host='localhost', port=27017):
        self._mongdb = MongoClient(host=host,port=port).db

    def insert_one(self,sql):
        self._mongdb.insert_one()



if __name__ == '__main__':
    # 连接服务器
    conn = MongoClient("localhost", 27017)
    db = conn.xzlmark  # 后面这个是选择数据库

    collection = db.test  # 后面这个是集合（表）
    # # 添加文档，插入一条数据
    # collection.insert_one({"name": "熊珍龙", "age": 31, "gender": 1, "address":"四川省达州市宣汉县", "isDelete":0})
    #
    # # 添加多条
    # collection.insert_many([{"name":"周莉",'gender':0,"age": 41,'address':'四川省达州市通川区','isDelete':0},
    # {"name":"向天秀",'gender':0,"age": 56,'address':'四川省达州市万源市','isDelete':0}
    #                         ])

    # 查询操作，注意：要加双引号，返回的结果是一个字典 ,如果所有，则括号里面不加条件即可
    res = collection.find({"age": {"$gt": 20}})
    for row in res:
        print(row['age'])

    # 统计查询出的数量

    count = collection.find().count()
    print('总条数有：%s' % count)

    # 根据ID进行查询
    res = collection.find({"_id": ObjectId("5d02653d7c40419c601695cc")})
    print(res[0])

    conn.close()