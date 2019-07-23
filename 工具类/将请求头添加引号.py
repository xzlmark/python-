"""
使用正则表达式将headers转换成python字典格式的工具函数
"""

import re

headers_str = """
:authority: www.zhihu.com
:method: POST
:path: /sc-profiler
:scheme: https
accept: */*
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
content-length: 250
content-type: application/json
cookie: _zap=613c6457-5875-4ab1-8643-76cec565b145; _xsrf=jCbKViHFThyAaG40vq7xUfQ8axu62CuF; d_c0="ACCt6mjdoA-PTkUZIO0AL4FQpce3aLLQ2Xk=|1561273497"; capsion_ticket="2|1:0|10:1561273523|14:capsion_ticket|44:NDIxZTFjNmJlZDMyNDZmZDkwNzY3MWVkOTczMzQ0MGE=|216756029e5bca8c4ce80f10618fef165147c1f8b8ca52e6baad329f4c65eab1"; z_c0="2|1:0|10:1561273612|4:z_c0|92:Mi4xMVNNRkJnQUFBQUFBSUszcWFOMmdEeVlBQUFCZ0FsVk5ESFA4WFFCNHBveTFMTm81clFwbklqSUkxZTVzU3hpU2F3|0619916a1c788a54f0029e751b4d2162e273b0ffb2c5feecc4096fcd6d6e7f98"; tst=r; q_c1=1ba8689a4e7e4c86bc6168bd5ea05ef6|1561273614000|1561273614000; tgw_l7_route=116a747939468d99065d12a386ab1c5f
origin: https://www.zhihu.com
referer: https://www.zhihu.com/
user-agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36


"""


pattern = '^(.*?): (.*)$'
#           1     2
for line in headers_str.splitlines():
    print(re.sub(pattern, '\'\\1\': \'\\2\',', line))