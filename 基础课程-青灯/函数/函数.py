# 函数可以通过关键字def来定义，后面根标识符名称，再根一对圆括号，其中可以包括一些变量的名称，再以冒号结尾
# global语句,如果需要给一个在程序顶层的变量赋值，那么必须通过global生命，如

x = 50


def func():
    global x
    print('x is ', x)
    x = 2
    print('changed global x to ', x)


func()
print('value of x is ', x)
