
birthdays={'熊珍龙':'7-8','王海东':'1-9'}
while True :
    print('请输入姓名:')
    name=input()
    if name=='':
      break

    if name in birthdays:
        print(birthdays[name]+'是'+name+'的生日')
    else :
        print('没有'+name+'的生日信息,请输入生日：')
        birthday=input()
        birthdays[name]=birthday
        print('生日信息更新成功')

 # keys()、values()、items()方法
for i in birthdays.keys():
    print(i)

for v in birthdays.values():
    print(v)

for j in birthdays.items():
    print(list(j))  #若不加list,则返回的是元组。

for i,v in birthdays.items():
    print('Key:'+i+'  ,Value:'+v)
