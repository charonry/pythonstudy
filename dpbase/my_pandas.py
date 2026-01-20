import numpy as np
import pandas as pd
import warnings
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', None)

"""
# series
# 方式一：直接创建
# s = pd.Series([10, 34, 2, None, 3, 41, np.nan, 5, 2, 6], index=['a', 'b', 'x', 'c', 'd', 'y', 'z', 'e', 'f', 'g'],
#               name='mySeries')
# 方式二：字典
# s = pd.Series({"a": "abc", "z": "xyz", "m": "nm"})
# s1 = pd.Series(s, index=['a', 'm'])
# demo1
# np.random.seed(42)
# scores = pd.Series(np.random.randint(50, 100, 10), index=['学生'+str(i) for i in range(1, 11)],
#                    name="student")
# scores_max = scores.max()
# scores_min = scores.min()
# scores_avg = scores.mean()
# scores_higher_avg = scores[scores > scores_avg]
# scores_higher_avg_count = scores_higher_avg.count()
# demo2
# temperatures = pd.Series([28, 31, 29, 32, 30, 27, 33], name='温度',
#                          index=['周一', '周二', '周三', '周四', '周五', '周六', '周日'])
# temperatures_high_count = temperatures[temperatures > 30].count()
# temperatures_avg = temperatures.mean()
# temperatures_sort = temperatures.sort_values(ascending=False)
# t1 = temperatures.diff().abs()
# t2 = t1.sort_values(ascending=False)[:2].keys()
# demo3
# prices = pd.Series([102.3, 103.5, 105.1, 104.8, 106.2, 107.0, 106.5, 108.1, 109.3, 110.2],
#                    index=pd.date_range('2025-01-01', periods=10), name='股票价格')
# prices_change = prices.pct_change()  # pct = percent
# prices_change_max = prices_change.idxmax()
# prices_change_min = prices_change.idxmin()
# prices_change_volatility = prices_change.std()
# demo3
# sales = pd.Series([120, 135, 145, 160, 155, 170, 180, 175, 190, 200, 210, 220],
#                   index=pd.date_range('2025-01-01', periods=12, freq='MS'), name='销售额')
# sales_q = sales.resample('QS').mean()
# sales_highest_month = sales.idxmax()
# sales_change = sales.pct_change()
# sales_compare = sales_change > 0
# sales_window = sales_compare.rolling(3)
# sales_plus_three = sales_change[sales_window.sum() == 3]
# demo4
# np.random.seed(42)
# hours_sales = pd.Series(np.random.randint(0, 100, 24),
#                          index=pd.date_range('2025-01-01', periods=24, freq='H'))
# sales_day = hours_sales.resample('D').sum()
# # 方式一
# sales_work = hours_sales.between_time("8:00", "22:00").sum()
# # 方式二
# sales_work = hours_sales[(hours_sales.index.hour >= 8) & (hours_sales.index.hour <= 22)]
# # 方式一
# sales_no_work = sales_day[0] - sales_work.sum()
# # 方式二
# sales_no_work = hours_sales.drop(sales_work.index).sum()
# # 方式一
# sales_top_three = hours_sales.sort_values(ascending=False).head(3)
# # 方式二
# sales_top_three = hours_sales.nlargest(3)
"""
"""
# DataFrame
# 方式一：直接创建
# s1 = pd.Series([1, 2, 3, 4, 5])
# s2 = pd.Series(['a', 'b', 'c', 'd', 'e'])
# df = pd.DataFrame({"num": s1, "char": s2})
# 方式二：字典
# df = pd.DataFrame({
#     "num": [11, 21, 31, 41, 41],
#     "name": ["a", "b", "c", 'd', 'd'],
#     "age": [20, 30, 30, 50, 50]
# }, index=[1, 2, 3, 4, 5], columns=['num', 'name', 'age'])
# demo1
# data = {
#     '姓名': ['张三', '李四', '王五', '赵六', '钱七'],
#     '语文': [85, 92, 78, 88, 95],
#     '数学': [90, 88, 85, 92, 80],
#     '英语': [75, 80, 88, 85, 90]
# }
# scores = pd.DataFrame(data)
# scores['总分'] = scores[['语文', '数学', '英语']].sum(axis=1)
# scores['平均分'] = scores[['语文', '数学', '英语']].mean(axis=1)
# scores_select = scores[(scores['语文'] > 90) | (scores['数学'] > 85)]
# scores_top3 = scores.nlargest(3, ['总分', '英语'])
# demo2
# data = {
#     '名称': ['A', 'B', 'C', 'D'],
#     '单价': [100, 150, 200, 120],
#     '销量': [50, 30, 20, 40]
# }
# product = pd.DataFrame(data)
# product['总额'] = product['单价'] * product['销量']
# demo3
# data = {
#     '用户ID': [101, 102, 103, 104, 105],
#     '用户名': ['张三', '李四', '王五', '赵六', '钱七'],
#     '商品类别': ['电子产品', '服饰', '电子产品', '家具', '服饰'],
#     '商品单价': [1200, 300, 800, 150, 200],
#     '购买数量': [1, 3, 2, 5, 4]
# }
# df = pd.DataFrame(data)
# df['总额'] = df['商品单价']*df['购买数量']
# all_avg = df['总额'].mean().round(2)
# num_3c = df[df['商品类别'] == '电子产品']['购买数量'].sum()
"""

df_csv = pd.read_csv("./resource/wps/employees.csv")
# df = pd.read_excel(r"D:\pythonSpace\pythonProject\resource\wps\demo01.xlsx")
# df.to_csv('./resource/wps/new.csv', index=False)
df_json = pd.read_json('./resource/txt/test.json')

