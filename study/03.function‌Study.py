"""
def func1(a, b=200):
    return a + b


# 可变参数： *args:将实参所有的位置参数接受，放置一个元祖里。可以传多个，也可以不传
def func(*args):
    return args


print(func())
print(func(1, 2, 3))


# 关键字参数：**kwargs：接受所有关键字参数后将其转换成一个字典赋值给kwargs
def fund(**kwargs):
    return kwargs


print(fund())
print(fund(name="charon", age=18))
"""

"""
first = [1, 2, 3, 4]
second = ['a', 'b', 'c', 'd', 'e']
third = zip(first, second)
for i in third:
    print(i, type(1), sep="\t")
print(third, type(third), sep="\t")
my_tuple = ['a', 'b', 'c', 'd', 'c']

a, b, *c = my_tuple
print(a, b, c, type(c), sep="\t")
my_dict = dict(name='Alice', age=30, city='New York')
a, *b = my_dict
print(a, b, type(b), sep="\t")
"""

