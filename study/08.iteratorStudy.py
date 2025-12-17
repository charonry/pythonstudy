"""
from collections.abc import Iterable
print(isinstance(123, Iterable))
"""

"""
my_list = [1, 2, 3]
# 第一种
# my_iter = iter(my_list)
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# 第二种
my_iter = my_list.__iter__()
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__next__())
print(my_iter.__dir__())
"""

"""
class MyIterator:
    def __init__(self):
        self.sum = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.sum == 10:
            raise StopIteration("终止迭代...没有数据")
        self.sum += 1
        return self.sum


myIterator = MyIterator()
print(myIterator)
for i in myIterator:
    print(i)
"""

"""
# 列表推导式
my_list = [i*5 for i in range(5)]
print(my_list)
# 生成器
gen = (i*5 for i in range(5))
print(gen.__next__())
print(next(gen))
"""


def myGenerator(n):
    li = []
    i = 0
    print("进入方法")
    while i < n:
        li.append(i)
        yield i
        i += 1
    print("my_list:", li)

my_gen = myGenerator(4)
for i in my_gen:
    print(i)

