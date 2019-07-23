while True :
    print('who are you?')
    name=input()
    if name!='xzl':
     continue
    print(name+': 请输入密码:')
    password=input()
    if password=='123':
     break
print('登录成功')
