# use {} 格式化字符串

s = 'hello {} !'
n = 18
print(s.format(n))
print('hello {} {}'.format(n, 'python'))  # 数字是可选，可以不写

# 还可以指定值的内容进行传参，适用于多次出现变量的情况
print('{b} hello {a} {b}'.format(a=n, b='python'))

# 对字符串用0填充  00001
print('{a:0>5}'.format(a=1))
print('{:*<5}'.format(1))  # 1****
print('{0:.3f}'.format(1/3))  # 保留3位小数
print('{0:_^11}'.format('hello'))  # 使用^定义字符串长度为11


# 还可以使用这种方式,注意是从0开始的
age = 20
name = 'xzl'
print('{0} is {1}'.format(name, age))
