i=100

while i<1000:
    g=int(str(i)[2])
    s = int(str(i)[1])
    b = int(str(i)[0])
    total=g**3+s**3+b**3
    if i==total:
        print('%s是水仙花数'%i)
    else:
        pass
    i=i+1