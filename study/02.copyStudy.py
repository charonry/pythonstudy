import copy as cp

firstNum = ['1', '2', '3']
secondNum = firstNum
firstNum.append('4')
print(firstNum, id(firstNum), secondNum, id(secondNum), sep="\t")

first = [1, 2, 3, [4, 5, 6]]
# 浅拷贝
second = cp.copy(first)
# 深拷贝
third = cp.deepcopy(first)
first[3].append(7)
print(first, id(first), sep="\t")
print(second, id(second), sep="\t")
print(third, id(third), sep="\t")
