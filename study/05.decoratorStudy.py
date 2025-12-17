"""
# 递归函数
def recursionAdd(num):
    if num == 1:
        return 1
    return num + recursionAdd(num - 1)


numSum = recursionAdd(100)
print(numSum)
"""

"""
# 闭包
def outer(n):
    def inner(m):
        return n + m

    return inner


closure_func = outer(10)
print(closure_func(5))
"""

"""
# 装饰器
def send():
    print("发送消息...")


def outer(fn):  # fn传入被装饰的函数名
    # 既包含原有功能，又含有新功能
    def inner():
        # 执行被装饰的函数
        fn()
    return inner


inner = outer(send)
inner()
"""

"""
# 语法糖
def outer(fn):
    def inner():
        print("添加的功能...")
        fn()

    return inner


@outer
def send():
    print("原有的功能")


send()
"""
