"""
class Person:
    def func(self):
        print("这是父类的方法")


class Child(Person):
    pass


class Boy(Child):
    def func(self):
        # 第一种 父类.方法名(self)
        # Person.func(self)
        # 第二种 推荐
        super().func()
        # 第三种 super(子类, self).func()
        # super(Boy, self).func()
        print("这是子类的方法")


boy = Boy()
boy.func()
print(Boy.__mro__)
"""

"""
class Annimal:
    def eat(self):
        print("这是动物同名方法")


class Dog(Annimal):
    def eat(self):
        print("这是狗同名方法")


class Cat(Annimal):
    def eat(self):
        print("这是猫同名方法")


# 多态性：定义一个统一接口，一个接口多个实现
def func(obj):
    obj.eat()


animal = Dog()
func(animal)
animal = Cat()
func(animal)
"""

"""
class Person:
    name = '类属性值'

    @classmethod
    def func(cls):  # cls代表类对象本身，本质是一个对象
        print("这是一个类方法：", cls)
        print("这是调用类属性：", cls.name)
        instance = cls()
        print("这是调用类方法：", instance.fund())

    def fund(self):
        print("这是另一个类方法")


# 第一种
# Person.func()
# 第二种
person = Person()
person.func()
"""

"""
# 整合
class Student:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def showInfo(self):
        print("我是{0},性别是{1}".format(self.name, self.__gender))

    @property
    def genderSet(self):
        return self.__gender

    @genderSet.setter
    def gender(self, gender):
        if gender == "男" or gender == "女":
            self.__gender = gender
        else:
            raise GenderException()


class GenderException(BaseException):
    def __init__(self):
        super().__init__()
        self.errMsg = "性别只能是男女"


try:
    stu = Student("chen", "男")
    stu.gender = "女"
    stu.showInfo()
except BaseException as e:
    print(type(e))
    print(e.errMsg)
    print("设置有误")
"""

"""
class Person:
    name = '类属性值'

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    @classmethod
    def func(cls):  # cls代表类本身
        print("这是一个类方法：", cls)
        print("这是调用类属性：", cls.name)
        instance = cls("b", 30)
        print(instance.gender)
        print("这是调用类方法：", instance.fund())

    def fund(self):
        print("这是另一个类方法")


# 第一种
Person.func()
# 第二种
person = Person('charon', 20)
print(person.gender)
person.func()
"""

"""
class Person:
    def __init__(self):
        print("这是初始化对象：", self)

    def __new__(cls, *args, **kwargs):
        print("这是创建类对象：", cls)
        # __new__()是静态方法，形参有cls，实参必须也要有cls
        res = super().__new__(cls)
        # 重写__new__()方法一定要return,否则python解释器得不到分配空间的对象引用，就不会执行__init__()方法
        return res


person = Person()
"""

"""
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product({self.name!r}, {self.price})"

    def __str__(self):
        return f"{self.name} - ¥{self.price}"


product = Product("笔记本电脑", 5999)
print("所有属性:", product.__dict__)  
print("官方表示:", repr(product))  
"""

