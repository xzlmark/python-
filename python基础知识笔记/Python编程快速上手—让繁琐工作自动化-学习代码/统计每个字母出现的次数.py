#统计一个字符串中各字母出现的次数
import pprint
message=input('请输入要统计的字符串：')
count={}

for i in message:
    count.setdefault(i,0)
    count[i]=count[i]+1
pprint.pprint(count)
