import requests
res=requests.get('https://api.github.com/user',auth=('user','pass'))
print('状态码：'+str(res.status_code))
print(res.headers['content-type'])
res.encoding='utf-8'  # 进行编码
print(res.text) # 输出文本内容，即是html文件内容
print(res.json())

# 重定向操作,如果直接输入http://github.com,则会定向到https://github.com
res1=requests.get('http://github.com',allow_redirects=False)
print(res1.status_code)  #

