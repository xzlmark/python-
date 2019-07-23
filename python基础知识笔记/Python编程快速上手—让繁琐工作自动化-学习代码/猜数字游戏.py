# 猜数字游戏，在7次范围内猜出随机产生的数字（1-20），每次猜后若不正确，告知大于还是小于正确的数字
import random
secretNum=random.randint(1,20)
print('猜数字游戏，猜1-20之间的一个数')

#定义猜的次数
for guessTimes in range(1,7):
     guess=int(input('请输入：'))

     if guess<secretNum:
         print('猜的数字太小')
     elif guess>secretNum:
         print('猜的数字太大')
     else:
         break
        
if guess==secretNum:
    print('好样的，你在'+str(guessTimes)+'次内猜正确了')
else:
    print('笨蛋，你猜的数字是：'+str(secretNum))
