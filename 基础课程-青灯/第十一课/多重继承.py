class Person:
    # 父类的构造方法
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # 如果父类的属性为私有属性，则子类虽然继承了，但无法直接调用,通过s1._Person__age 调用

    def say_age(self):
        print(self.name, '年龄是：', self.__age)

class Student(Person):
    def __init__(self, name, age, score):
        self.scroe = score
        Person.__init__(self, name, age)  # 构造函数中包含调用父类构造函数。根据需要，不是必须。子类并不会自动调用父类的\
                                        #__init__(),我们必须显式的调用它。
s1=Student('熊珍龙', 18, 100)
s1.say_age()
print(dir(s1))  # dir()打印的是对象所有的属性和方法
print(s1._Person__age)  # 调用父类的私有属性
print(Student.mro())
