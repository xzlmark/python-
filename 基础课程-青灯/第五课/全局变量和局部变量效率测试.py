import time
import math
def test01():
    start=time.time()
    for i in range(10000000):
        math.sqrt(30)
    end=time.time()
    print('耗时：{}'.format((end-start)))
def test02():
    b=math.sqrt  # 将全局变量math.sqrt赋值给局部变量b
    start=time.time()
    for i in range(10000000):
        b(30)
    end=time.time()
    print('耗时：{}'.format((end-start)))

test01()
test02()

