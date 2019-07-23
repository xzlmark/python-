import requests,bs4,os
totou_count=10
while totou_count >0:
  try:
    url='http://s1bfd.d39jcrlyy.com/190528/%E5%81%B7%E6%8B%8D%E8%87%AA%E6%8B%8D/%E8%A6%81%E4%B9%B3%E4%BA%A4%E5%90%97%E6%8C%A4%E5%A5%BD%E4%BA%86[17P]/01.jpg'
    print(url)
    res=requests.get(url)
    print(len(res.text))
    res.raise_for_status()
    imageFile=open(os.path.join('image',os.path.basename(url)),'wb')
    for chunk in res.iter_content(100000):
      imageFile.write(chunk)
    imageFile.close()
    break
  except Exception:
      totou_count=totou_count-1
      print('异常')
