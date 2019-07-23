import re
'''切割字符串'''
str='xzl is a good     man'
print(str.split(' '))   # 用字符串方法只能切割空一个空格，不满足条件
print(re.split(' +',str))
'''
输出结果为：
['xzl', 'is', 'a', 'good', '', '', '', '', 'man']
['xzl', 'is', 'a', 'good', 'man']
'''


'''finditer() 返回的是一个迭代器'''
str='xzl is a good man ,xzl is a nice man'
d=re.finditer('(xzl)',str)
print(d)
# 输出结果为： <callable_iterator object at 0x0000000002378EF0>


'''
字符串的替换和修改
sub(pattern, repl, string, count=0, flags=0) 再目标字符串中以正则表达式的规则匹配字符串，再把他们替换成指定的字符串
    repl:指定的用来替换的字符串
    count:最多替换次数；如果不指定，则全部替换
subn()：与sub功能一样
区别：前者返回一个被替换的字符串，后者返回的一个元组，第一个元素是被替换的字符串，第二个元素表示被替换的次数
'''
str='xzl is a good man ,xzl is a nice man'
print(re.sub(r'(xzl)','zhouli',str))
print(re.subn(r'(xzl)','zhouli',str))
'''
输出结果为：
zhouli is a good man ,zhouli is a nice man
('zhouli is a good man ,zhouli is a nice man', 2)
'''


'''
分组
概念：除了简单的判断是否匹配之外，正则表达式还有提取子串的功能，用()表示就是提取分组
'''
str='0818-5713329'
m=re.match(r'(\d{4})-(\d{7})',str)
print(m.groups())  # 查看各组的匹配情况
print(m.group(0))  # 表示原始的str字符串
print(m.group(1))
print(m.group(2))
'''
输出结果为：
('0818', '5713329')
0818-5713329
0818
5713329
'''

'''
编译：当我们使用正则表达式时，re模块会做两件事
1、编译正则表达式，如果正则表达式本身不合法，会报错
2、用编译后的正则表达式去匹配对象
compile(pattern, flags=0) 
'''
pat = r'^1(([3578]\d)|(47))\d{8}$'
# 编译正则表达式，后面就可以用编译后的对象调用相应的方法
re_telephon=re.compile(pat)
print(re_telephon.match("18228647002"))   # 这里就可以直接传入字符串参数就可以了，其他方法类似
# 输出<re.Match object; span=(0, 11), match='18228647002'>