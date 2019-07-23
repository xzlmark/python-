import redis


class XzlRedis:
    def __init__(self, password, host='localhost', port=6379):
        self.__redis = redis.StrictRedis(host=host, port=port, password=password)

    def set(self, key, value):
        self.__redis.set(key, value)

    def get(self, key):
        if self.__redis.exists(key):
            return self.__redis.get(key)
        else:
            return ""


if __name__ == '__main__':
    xzl = XzlRedis('123456')
    # 存入string
    xzl.set('gender', 1)

    res = xzl.get('name')
    print(res)
