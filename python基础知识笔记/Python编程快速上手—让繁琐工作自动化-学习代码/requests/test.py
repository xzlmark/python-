import requests,bs4
exampleFile=open('test.html')
soup=bs4.BeautifulSoup(exampleFile.read(),'html5lib')
print(type(soup))
elems=soup.select('#xzl')
print(len(elems))
print(elems[0].getText())
