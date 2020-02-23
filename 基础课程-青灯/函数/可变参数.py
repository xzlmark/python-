# 如果向定义的函数能够有任意数量的变量，也就是参数数量是可变的，可以通过使用星号来实现


def total(a=5, *numbers, **phonebook):
    print('a', a)
    # 遍历元组中的所有项目，*保存的是位置参数,是元组
    for single_item in numbers:
        print('single_item', single_item)
    # 遍历字典中的所有项目，**保存的是所有关键字参数，是字典
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)


print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1260))
