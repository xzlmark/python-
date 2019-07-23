import redis

# 建立连接
r = redis.StrictRedis(host='localhost', port=6379, password=123456)

# 注意：写的方式有2种，一种是根据类型不同，调用相应的方法
r.set('name', '熊珍龙')


# 第二种，pipeline。缓冲多条命令，然后依次执行，减少服务器-客户端之间的TCP数据包
pipe = r.pipeline()
pipe.set('p1', 'ice')
pipe.set('p2', 'ice')
pipe.set('p3', 'ice')
pipe.execute()
print(r.get('name'))
