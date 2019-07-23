# 定义类，用class关键字，括号里面写object或则不用写
class Person(object):
    def __init__(self):
        self.name = 'Tom'
        print('这个是初始化方法，专门 用来定义一个类 具有哪些属性的方法')

    def eat(self, name):   # 属性可以通过类方法传入
        print('%s 吃东西' % name)

    def paly(self):
        print('%s玩游戏' % self.name)

    def drink(self, name):
        print('{}喝饮料'.format(name))


marry = Person()
marry.eat('marry')
marry.paly()
marry.drink('marry')