'''
水仙花数（Narcissistic number）也被称为超完全数字不变数（pluperfect digital invariant, PPDI）、
自恋数、自幂数、阿姆斯壮数或阿姆斯特朗数（Armstrong number），水仙花数是指一个 3 位数，它的每个
位上的数字的 3次幂之和等于它本身（例如：1^3 + 5^3+ 3^3 = 153）。
'''

num=int(input('请输入一个三位数：'))
# 判断是三位数
if num>100 and num<1000:
    str_num=str(num)
    b_wei=int(str_num[0])
    s_wei=int(str_num[1])
    g_wei = int(str_num[2])
    if (b_wei**3+s_wei**3+g_wei**3)==num:
        print('%s是水仙花数' % num)
    else:
        print('%s不是水仙花数' % num)
else:
    print('输入的不是三位数')