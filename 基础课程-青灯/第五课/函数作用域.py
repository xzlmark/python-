num=0
# 局部变量与全局变量，f是一个函数
def f():
    num=10  #局部变量，优先级大于外部;局部变量的修改并不会改变全局
    print(num)

print(num)
f()
print(num)