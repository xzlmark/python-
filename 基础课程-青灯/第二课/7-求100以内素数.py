"""
素数序列-生成器方式实现
"""


class PrimeNum(object):

    """
    返回素数可迭代序列
    """

    @staticmethod
    def __nature_generator():
        # 生成计数的自然数序列
        n = 1
        while True:
            n += 2
            yield n

    @staticmethod
    def __filter(n):
        # 过滤掉当前素数倍数的非素数
        return lambda x: x % n > 0

    def prime(self):
        # 返回生成器的第一个值
        yield 2
        # 生成器序列
        prime_generator = self.__nature_generator()
        while True:
            # 弹出下个素数
            n = next(prime_generator)
            yield n
            # 过滤当前序列
            prime_generator = filter(self.__filter(n), prime_generator)

    def __call__(self, *args, **kwargs):
        return self.prime()

    def limit(self, num):
        ls = []
        p = self.prime()
        for i in range(0, num):
            ls.append(next(p))
        return ls


if __name__ == '__main__':
    p = PrimeNum()
    a = p.limit(100)
    print(a)