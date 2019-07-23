# 用%s 占位
s='hello %s !'
n=18

print(s % n)
print('hello %.2f !' % n)

s1='hello %d %s !' % (n,'python')
print(s1)