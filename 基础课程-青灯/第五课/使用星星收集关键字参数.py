
def f(x,k,b):
    return x*k+b

# **kwargs函数在传参得过程中，使用的字典；使用*args, **kwargs收集所有参数
def get_info(*args,**kwargs):
    print(args)
    # args 是一个元组
    print(kwargs)
    return f(*args,**kwargs)

# 下面调用得时候，参数需要和前面一致
print(get_info(6,6,b=20))
