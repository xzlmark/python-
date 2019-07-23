#下载https://www.se0504.com:2087/news-read-id-212.html-11756的所有的图片并保存在硬盘上
import requests,bs4,os
'''def get_proxy():
    return requests.get('http://127.0.0.1:5010/get/').content
def delete_proxy(proxy):
    requests.get('http://127.0.0.1:5010/delete/?proxy={}'.format(proxy))'''
proxy = {'http': '106.110.65.109:8118'}


for i in range(13506,13836):
    url='https://www.se0504.com:2087/news-read-id-%s.html' % i
    os.makedirs('C:\\image\\image'+str(i),exist_ok=True) #保存在 ./image
    #下载页面
    print('下载的页面是：%s...' % url)
    res=requests.get(url,proxies=proxy)
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text,'html5lib')
    # 找到图片的url
    comicElem=soup.select('p img')
    if comicElem==[]:
       print('没找到图片...')
    else:
       print(len(comicElem))
       for j in range(len(comicElem)):
         comicUrl='https://www.se0504.com:2087'+comicElem[j].get('src')
         #下载图片
         print('下载图片 %s...' % (comicUrl))
         res=requests.get(comicUrl)
         res.raise_for_status()
        
         #保存文件,os.path.basename()返回的是最后的文件名
         imageFile=open(os.path.join('C:\\image\\image'+str(i),os.path.basename(comicUrl)),'wb')
         for chunk in res.iter_content(10000):
            imageFile.write(chunk)
         imageFile.close()
print('下载完毕')
