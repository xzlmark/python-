# k 指定默认参数5，b指定默认参数6
# 默认参数不传参就使用默认参数；如果有，就对默认参数进行覆盖
def f(x, k=5, b=6):
    print(x,k,b)
    return k*x+b

# 函数得多态
print(f(6))
print(f(x=6,b=7))
print(f(x=6,k=6,b=7))
