# 用while

# i=1
# while i <=9:
#     j=1
#     while j<=i:
#         print('%s*%s=%s'%(j,i,i*j),end='\t')
#         j+=1
#     print()
#     i=i+1

# 用for循环
for m in range(1,10):
    for n in range(1,m+1):
        print('{0}*{1}={2}'.format(m,n,m*n),end='\t')
    print()