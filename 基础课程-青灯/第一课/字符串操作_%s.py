# 用%s 占位
s = 'hello %s !'
n = 18

print(s % n)
print('hello %.2f !' % n)

s1 = 'hello %d %s !' % (n, 'python')
print(s1)

# 如果一行中有\，则表示数据还没有结束，可以继续换行后写
print('this is a \
good boy!')

# 原始字符串，用r或R来表示
r = r'this is a good boy!\n ?'
print(r)
r1= R'this is a good man!'
print(r1)