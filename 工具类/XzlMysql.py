import mysql.connector


class XzlMysql:
    def __init__(self, host, user, password, dbName):
        self.host = host
        self.user = user
        self.password = password
        self.dbName = dbName

    # 连接数据库
    def connect(self):
        self.db = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.dbName)
        self.curosor = self.db.cursor()

    # 关闭游标和数据库
    def close(self):
        self.curosor.close()
        self.db.close()

    # 获取一条数据
    def get_one(self, sql):
        res = None
        try:
            self.connect()
            self.curosor.execute(sql)
            res = self.curosor.fetchone()
            self.close()
        except Exception as ex:
            print('查询失败:{}'.format(ex) )
        return res

    # 获取所有结果,结果为元组类型
    def get_all(self, sql):
        res = ()
        try:
            self.connect()
            self.curosor.execute(sql)
            res = self.curosor.fetchall()
            self.close()
        except Exception as ex:
            print('查询失败{}'.format(ex))
        return res

    # 插入操作
    def insert(self, sql):
        return self.__edit(sql)

    # 更新操作
    def update(self, sql):
        return self.__edit(sql)

    # 删除操作
    def delete(self, sql):
        return self.__edit(sql)

    # 增、删、改操作都需要使用这个下面这个方法
    def __edit(self, sql):
        count = 0   # 统计影响的结果数
        try:
            self.connect()
            self.curosor.execute(sql)
            count = self.db.commit()
            self.close()
        except Exception as ex:
            print('事务提交失败：{}'.format(ex))
            self.db.rollback()
        return count
