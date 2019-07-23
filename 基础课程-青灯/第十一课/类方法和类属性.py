class Student:
    company = 'SXT'   # 类属性
    @classmethod
    def printCompany(cls):
        print(cls.company)


print(Student.company)
Student.printCompany()

s=Student()
s.printCompany()