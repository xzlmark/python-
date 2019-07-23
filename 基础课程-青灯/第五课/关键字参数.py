# 关键字参数,与位置没有关系
def f(x, k, b):
    return k*x+b

print(f(x=6,k=5,b=6))
print(f(k=5,x=6,b=6))    #  与顺序没有关系