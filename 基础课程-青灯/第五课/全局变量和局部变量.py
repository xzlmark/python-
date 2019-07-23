a=100 # 全局变量
def f1():
    global a # 如果要在函数内改变全局变量的值，增加global关键字申明
    print(a) # 打印全局变量a的值
    a=300
f1()
print(a) # 经过函数修改全局变量，a的值被修改了

