'''
编写一个函数，它以一个列表值作为参数，返回一个字符串。该字符串包含所有
表项，表项之间以逗号和空格分隔，并在最后一个表项之前插入and.
'''
def spam(name):
    for i in range(len(name)):
        if i==len(name)-1:
            print('and '+name[i])
        else:
            print(name[i]+',',end=' ')
name=[]
while True:
    keyName=input('请输入人名：')
    if keyName=='':
      break
    name=name+[keyName]
spam(name)
