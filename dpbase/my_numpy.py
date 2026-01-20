import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import matplotlib.pyplot as plt  # 必须导入matplotlib
# plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# plt.rcParams['axes.unicode_minus'] = False
#
#
# def numpy_sum(n):
#     a = np.arange(n) ** 2
#     b = np.arange(n) ** 3
#     return a + b
#
#
# pytimes = [1.06*1000, 104*1000, 10.4*1000*100]
# nptimes = [0.16, 424, 114*1000]
# df = pd.DataFrame({
#     "pytimes": pytimes,
#     "nptimes": nptimes
# })

# x = np.array([1, 2, 3, 4, 5])
# X = np.array([
#     [1, 2, 3],
#     [6, 7, 9]
# ])
# # 结构
# x.shape
# # 维度
# x.ndim
# # 长度
# x.size
# # 类型
# x.dtype
#
# # 数字全为1的维度数据 zeros empty full
# np.ones((2, 3))
# # 数字全为1的维度X数据 zeros_like empty_like full_like
# np.ones_like(X)
# # 随机数
# np.random.randn(3,2,4)
#
# A = np.arange(10).reshape(2,5)

# x1 = np.arange(10)
# X = np.arange(20).reshape(4, 5)
# # numpy切片修改会修改原来的数组
# A = X[:2, 2:3]
# # 神奇索引
# x1 = np.arange(2, 22, 2)
# index = np.array([[0, 2], [4, 8]])
# x2 = x1[index]
# arr = np.random.randint(1, 100, 10)
# arr1 = arr[arr.argsort()[-3:]]
# arr2 = X[[0,2,3],[1,2,4]]
# ARR3 = X[X[:,3]>8]
#
# condition = (x1%2==0)|(x1>7)
# arr4 = x1[condition]

# np.random.seed(666)
# x = np.linspace(-10,10,100)
# y = np.sin(x) + np.random.rand(len(x))
# plt.plot(x,y)
# plt.show()

# arr = np.arange(12).reshape(3, 4)
# ARR = np.random.randint(10,100,(3,4))







