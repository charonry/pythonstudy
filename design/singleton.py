## 单例模式
"""
# 1.重写__new__()方法
class Singleton:
    obj = None

    def __new__(cls, *args, **kwargs):
        if cls.obj is None:
            cls.obj = super().__new__(cls)
        return cls.obj

    def __init__(self):
        pass


s1 = Singleton()
print("s1:", s1)
s2 = Singleton()
print("s2:", s2)
"""

"""
# 2.装饰器实现
def outer(fn):
    _ins = {}

    def inner():
        if fn not in _ins:
            _ins[fn] = fn()
        return _ins[fn]
    return inner


@outer
class A:
    pass


print(A())
print(A())
"""

"""
# 3.元类实现
class A:
    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'charon'):
            cls.charon = super().__new__(cls)
        return cls.charon


print(A("张三"))
print(A("李四"))
"""



