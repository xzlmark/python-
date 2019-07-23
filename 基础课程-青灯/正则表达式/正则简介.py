import re
str='www.baidu.com'
print(re.match('www',str))  # 能匹配
print(re.match('www','ww.baid'))  # 不能匹配
print(re.match('www','ww.baidwww'))  # 不是起始位置，不能匹配
print(re.match('www','wwW.baidu.com'))  # 不能匹配,大小写不同
print(re.match('www','wwW.baidu.com',flags=re.I))  # 能匹配,忽略大小写

print('-------------------------')

re.search()
re.findall()