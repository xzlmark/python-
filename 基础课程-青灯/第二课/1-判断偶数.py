
num =int(input('请输入数字：'))

if num %2==0:
    print('%s是2的倍数' % num)
elif num % 3==0:
    print('%s是3的倍数' % num)
elif num % 5==0:
    print('%s是5的倍数'% num)
elif num % 7==0:
    print('%s是7的倍数'% num)
else:
    print('%s是2、3、5、7其他数字的倍数'% num)
