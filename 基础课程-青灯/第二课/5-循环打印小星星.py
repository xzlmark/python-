# 第一种思路是用* 来实现
'''
i=1
while i<=10:
    print('*'* i)
    i+=1
'''
# 第二种思路是循环嵌套

i=1
while i<=5:
    j=1
    while j<=i:
        print('*',end='')
        j+=1
    print()
    i+=1