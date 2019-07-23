#下载https://xkcd.com 中所有的漫画
import requests,bs4,os
url='http://xkcd.com'  #开始的url
os.makedirs('xkcd',exist_ok=True) #保存在 ./xkcd
while not url.endswith('#'):
    #下载页面
    print('下载的页面是：%s...' % url)
    res=requests.get(url)
    res.raise_for_status()
    soup=bs4.BeautifulSoup(res.text,'html5lib')

    # 找到图片的url
    comicElem=soup.select('#comic img')
    if comicElem==[]:
        print('没找到图片...')
    else:
        comicUrl='http:'+comicElem[0].get('src')
        #下载图片
        print('下载图片 %s...' % (comicUrl))
        res=requests.get(comicUrl)
        res.raise_for_status()

        
        #保存文件,os.path.basename()返回的是最后的文件名
        imageFile=open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

        
    #得到前一个按钮的url
    prevLink=soup.select('a[rel="prev"]')[0]
    url='http://xkcd.com'+prevLink.get('href')
print('完成')

