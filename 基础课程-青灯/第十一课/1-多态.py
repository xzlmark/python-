class Animal():
    def __init__(self,name):
        self.name=name

    def talk(self):
        print('..........')


class Cat(Animal):
    def talk(self):
        print('喵喵叫')


class Dog(Animal):
    def talk(self):
        print('旺旺叫')


# 接口函数，多态形态，也就是不关心obj的类型，根据传入的类型不同，调用的方法也就不用
def func(obj):
    obj.talk()


c1=Cat('咪咪')
d1=Dog('旺财')

# 多态，也就是同一个接口函数，只是传入的对象不同就调用不同的方法
func(c1)
func(d1)