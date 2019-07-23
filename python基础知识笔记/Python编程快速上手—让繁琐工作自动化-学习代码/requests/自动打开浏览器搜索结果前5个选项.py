#自动打开百度搜索，将前面列举的前5项打开
import requests,sys,webbrowser,bs4

print('baidu...')
#注意，https实验不成功
res=requests.get('http://www.baidu.com/s?wd='+' '.join(sys.argv[1:]))
res.raise_for_status()
# print(res.text)
soup=bs4.BeautifulSoup(res.text,'html5lib')
linkElems=soup.select('.t a')
# print(linkElems)
numOpen=min(5,len(linkElems))
print(numOpen)
for i in range(numOpen):
    webbrowser.open(linkElems[i].get('href'))
#    print(linkElems[i].get('href'))
