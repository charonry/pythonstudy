""" list
a = [1, 22, 3]
print(2 in a)
b = ['a', 'bc', 'd']
print('bc' in b)
print(a.count(22))
del a[2]
print(a)
c = [i for i in range(1, 11) if i % 2 == 1]
print(c, type(c))
"""

""" tuple
a = (1,)
print(type(a))
"""

""" dict
my_dict = dict(name='Alice', age=30, city='New York')
print(type(my_dict.keys()))
print(type(my_dict.values()))
my_type = my_dict.items()
print(my_type, type(my_type), len(my_type), sep="\t")
my_list = [my_dict.keys()]
print(my_list, type(my_list), len(my_list), sep="\t")
"""

""" set
my_set = {'a', 'b', 'c', 'd'}
my_set.discard('e')
my_set1 = {1, 2, 3, 4}
my_set2 = {1, '2', '3', 4}
my_type1 = my_set1 & my_set2
my_type2 = my_set1 | my_set2
print(my_type1, type(my_type1), sep="\t")
print(my_type2, type(my_type2), sep="\t")
"""


