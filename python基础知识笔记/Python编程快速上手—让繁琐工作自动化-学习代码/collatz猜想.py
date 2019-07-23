# 编写一个名为collatz()的函数，它有一个名为number的参数：
# 如果参数是偶数，那么collatz()就打印出number//2,并返回该值；
# 如果number是奇数，那么collatz()就打印，并返回3*number+1。
# 然后编写一个程序，让用户输入一个整数，并不断对这个数调用collatz()，直到函数返回值1
import sys
def collatz(number):
    print(number)
    if number==1:
        sys.exit()
    elif number % 2==0:
        t= number//2
        collatz(t)
    else:
         t= number*3+1
         collatz(t)
   
# if __name__ == '__main__' 我们简单的理解就是：
# 如果模块是被直接运行的，则代码块被运行，如果模块是被导入的，则代码块不被运行

if __name__=='__main__':
    n=input('请输入数字：')
    try:
        n=int(n)
        collatz(n)
    except ValueError:
         print('请输入整数')
