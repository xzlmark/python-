myAge=int(input())
if myAge<=18:#有:的下一行必须要有缩进，否则要报错用空格或则tab
    print('你是未成年人')
elif myAge>18 and myAge<=60:
    print('你是成年人')
else:
    print('你是老年人啦。。。')
