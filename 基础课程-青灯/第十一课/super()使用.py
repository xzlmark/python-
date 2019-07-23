class A:
    def say(self):
        print('say AAA')
class B(A):
    def say(self):
        super().say()
        print('say BBB')
b=B()
b.say()