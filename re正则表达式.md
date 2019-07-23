# 正则表达式

python里面内置了re模块，提供了正则表达式模式；

re模块使python语言拥有了全部的正则表达式功能

## re.match()

```python
match(pattern, string, flags=0)

"""Try to apply the pattern at the start of the string, returning
a Match object, or None if no match was found."""
```

pattern:匹配的正则表达式，string：要匹配的字符串；flags:标志位，用于控制正则表达式的匹配方式，常见的值有:

​	re.I 	忽略大小写

​	re.L	做本地户识别

​	re.M	多行匹配，影响^和$

​	re.S	是.匹配包括换行符在内的所有字符

​	re.U	根据Unicode字符集解析字符，影响\w \W \b \B

​	re.X	使我们以更灵活的格式理解正则表达式

功能：从字符串的**起始位置**匹配一个正则表达式，如果不是起始位置匹配不成功则返回None

```python
import re
str='www.baidu.com'
print(re.match('www',str))  # 能匹配
print(re.match('www','ww.baid'))  # 不能匹配
print(re.match('www','ww.baidwww'))  # 不是起始位置，不能匹配
print(re.match('www','wwW.baidu.com'))  # 不能匹配,大小写不同
print(re.match('www','wwW.baidu.com',flags=re.I))  # 能匹配,忽略大小写
```



## re.search()

```
search(pattern, string, flags=0)

""Scan through string looking for a match to the pattern, returning
a Match object, or None if no match was found."""

功能：扫描整个字符串，并返回第一个成功的匹配

```

## re.finall()

```
findall(pattern, string, flags=0)
扫描整个字符串，并返回结果列表
```



# 正则表达式的元字符

 .				匹配换行符意外的任意字符

[0123456789]	   []是字符集合，表示匹配括号中包含的任意一个字符

[xzlmark]		   匹配字符串中任意一个字符

**[a-z]**			  匹配任意小写字母

**[A-Z]**			 匹配任意大写字母

**[0-9]**  或 \d	        匹配任意数字，类似于[0123456789]

[0-9a-zA-Z_] 或\w     匹配任意数字、字母和下划线

[^0-9a-zA-Z]  或\W    匹配除数字、字母和下划线

[^xzlmark]		  匹配除了xzlmark以外的所有字符

**[^0-9]** 或 \D     	  匹配所有的非数字字符

\s 或[ \t\f\n\r]	     匹配任意的空白字符（空格、制表符、回车、换页、换行）

\S 或[^ \t\r\n\f]		匹配任意的非空白字符



## 锚字符

^ 	行首匹配，和在[^]不是一个意思

$	 行尾匹配

\A	匹配字符串开始，它和^ 的区别是，\A只匹配整个字符串的开头，即使在re.M模式下也不会匹配它行的行首

\Z	匹配字符串结束，它和$的区别是，\Z只匹配整个字符串的结尾，即使在re.M模式下也不会匹配它行的行尾

\b	匹配一个单词的边界，也就是值单词和空格间的位置

​	    'er\b'可以匹配never，不能匹配nerve

\B	匹配非单词边界

## 匹配多个字符

说明：下方的x、y、z均为假设的普通字符，不是正则表达式的元字符

(xyz)		匹配小括号内的xyz(作为一个整体去匹配)

x?		     匹配0或1个x

x*		      匹配0个或则任意多个x

x+		     匹配至少一个

x{n}		   匹配确定的n个x(n是一个非负整数)

x{n，}		匹配至少n个x(n是一个非负整数)

x{n，m}	     匹配至少n个最多m个x。注意：n<=m

x|y		     表示或，匹配的是x或y

注意：*?   +?   x?  表示最小匹配

## 高级用法

```python
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
```

