#use python's open() and write() method save files
#不同的是，这里一定要用wb参数,才能保存该文本为Unicode编码
import requests
res=requests.get('http://www.baidu.com/')
res.raise_for_status()
newFile=open('newFile.txt','wb')
#iter_content()方法在循环的每次迭代中，返回一段内容，每一段都是bytes数据，一般10000是个不错的选择
for content in res.iter_content(100000):
    newFile.write(content)
newFile.close()
