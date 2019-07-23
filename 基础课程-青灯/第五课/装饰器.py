import time


# 传入函数名
def timer(func):
    # 给函数添加的功能
    def ware(*args, **kwargs):
        start_time = time.time()
        time.sleep(0.1)
        # 函数的原本功能
        func(*args, **kwargs)
        print(time.time()-start_time)
    # 返回一个函数对象,千万不能家括号，否则会出错
    return ware


@timer
def add(x, k):
    return x+k


@timer
def sub(x, k):
    return x-k


@timer
def multi(x, k, b):
    return x*k*b


add(5, 6)
sub(2, 3)
multi(4, 3, 200)
