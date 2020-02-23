# 默认参数值，可以通过=来指定

def say(message, times=1):
    print(message * times)


say('hello')
say('world', 5)
