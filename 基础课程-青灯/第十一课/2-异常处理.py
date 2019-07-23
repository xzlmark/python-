# 异常处理的几种方式
# 1：常规的异常处理,用try excpt进行处理
# print('test1.....')
# try:
#     open('text.txt')
# except Exception as ex:
#     print(ex)
#     print('tst2....')

# 2:用try except else进行处理，try:执行可能会出错的语句，except：如果try里面的语句无法正确执行，那么执行except
#  里面的语句；else：如果try里面的语句可以正常执行，那么就执行else里面的语句

# try:
#     print(1)
# except:
#     print('出现异常')
# else:
#     print('没有出现异常')

# 3.try except finally进行处理.finally的意思就是不管上面出现异常与否，都要执行下面的语句
# try:
#     open('test.txt')
# except:
#     print('出现异常')
# finally:
#     print('test2.....')

# 4.嵌套使用.这个给if判断道理一样，try 后面可以不用except，直接用finally语句,如下面，如果嵌套中用except，永远也不会执行
# import time
# try:
#     f = open('test.txt')
#     try:
#         while True:
#             content = f.readline()
#             if len(content) == 0:
#                 break
#             time.sleep(2)
#             print(content)
#     finally:
#         f.close()
#         print('关闭文件')
# except:
#     print('没有这个文件')

# 5.自定义异常


class ShortInputException(Exception):
    def __init__(self,length,atleast):
        self.length=length
        self.atleast=atleast


def main():
    s = input('请输入内容:')
    try:
        if len(s) < 3:
            raise ShortInputException(len(s), 3)
    except ShortInputException as ex:
        print('出现异常：%s,输入的字符串长度是%d,长度至少是：%d' % (ex, len(s), 3))
    else:
        print('没有异常')


main()
