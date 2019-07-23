#test=['熊珍龙','王轩','刘小龙','王海东','朱彬']
# print(test[1:3])
# print(len(test))
#test[0]='熊波'
#print(test)
#del test[4]
#print(test)


办公室人名=[]
while True:
    print('请输入第'+str(len(办公室人名)+1)+'人姓名:'+'（输入空终止）')
    name=input()
    if name=='':
        break
    办公室人名=办公室人名+[name]
print('办公室人有：')
#for i in range(len(办公室人名)):
#    print(' '+办公室人名[i])

for name in 办公室人名:
    print(' '+name)
print (办公室人名.index('熊珍龙'))
