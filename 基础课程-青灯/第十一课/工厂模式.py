class CarFactory:
    def crateCar(self,brand):
        if brand=='奔驰':
            return BenZ()
        elif brand=='大众':
            return DaZhong()
        else:
            return '未知'

class BenZ:
    pass

class DaZhong:
    pass
factory=CarFactory()
c1=factory.crateCar('奔驰')
c2=factory.crateCar('大众')
print(c1)
print(c2)