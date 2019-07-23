#requests库
import requests
#返回Response对象
res=requests.get('http://www.baidu.com')
#查看对象类型
print(type(res))
#http协议中OK的状态码是200 ,可以根据这个判断是否下载成功
if res.status_code==requests.codes.ok:  # 状态码查询对象
    print('请求成功:'+str(res.status_code))
else:
    print('请求不成功:'+str(res.status_code))
#下载的内容保存在res.text里面
print(len(res.text))
print(res.text[0:100])


 #最科学的是通过下面的方式来判断下载是否成功,成功则返回None，不成功则抛出异常
res1=requests.get('http://baidu.com/')
try:
    res1.raise_for_status()
    print(res1.headers['content-type'])   # 这么访问就可以知道数据类型，如果是json就可以用res.json()产生json对象
except Exception as exc:
    print('出错了：%s' % (exc))

