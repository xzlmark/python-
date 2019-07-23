import shelve
# 利用shelve模块，可以将Pyhon程序中的变量保存到二进制的shelf文件中

shelFile=shelve.open('mydata')
人名=['xzl','mark']
shelFile['人名']=人名
shelFile.close()

#可以用keys()和values()读取shelve内容
sheFile1=shelve.open('mydata')
print(list(sheFile1.keys()))
print(list(sheFile1.values()))
sheFile1.close()

