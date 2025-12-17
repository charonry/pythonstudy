"""
# 线程池-同异步
from multiprocessing import Pool
import time
import os

def func(n):
    print("执行子任务")
    time.sleep(2)
    return n*2

if __name__ == "__main__":
    pool = Pool(3)
    my_list = []
    for i in range(5):
        # 异步执行
        result = pool.apply_async(func, args=(i,)) # pool.apply同步；apply_async异步
        my_list.append(result)  # 获取返回结果 result.get()会导致阻塞，异步失效
    # 关闭进程池。关闭后不在接受新的请求：不关闭导致只能处理定义容量的子任务数
    pool.close()
    # 等待进程池中所有子任务完成
    pool.join()
    print(my_list)
"""

"""
from multiprocessing import Pool, Manager
import os


def rd(q):
    print(f"rd启动{os.getpid()},父进程是{os.getppid()}")
    for i in range(q.qsize()):
        print(f"取出数据{q.get()}")


def wd(q, data):
    print(f"wd启动{os.getpid()},父进程是{os.getppid()}")
    for i in data:
        print(f"当前写入内容：", i)
        q.put(i)


if __name__ == '__main__':
    print(f"主进程pid{os.getpid()}")
    queue = Manager().Queue()
    pool = Pool()
    str = "charon"
    pool.apply_async(wd, args=(queue, str))
    pool.apply_async(rd, args=(queue,))
    pool.close()
    pool.join()
    print("结束了")
"""

"""
import time


def func():
    while True:
        yield "子任务一"
        time.sleep(0.5)


def fund():
    while True:
        yield "子任务二"
        time.sleep(0.5)


if __name__ == '__main__':
    fc = func()
    fd = fund()
    while True:
        print(next(fc))
        print(next(fd))
"""

"""
from greenlet import greenlet


def func():
    print("子任务一开始")
    fd.switch()
    print("子任务一结束")
    fd.switch()


def fund():
    print("子任务二开始")
    fc.switch()
    print("子任务二结束")


if __name__ == '__main__':
    # 创建greenlet
    fc = greenlet(func)
    fd = greenlet(fund)
    # 切换fc执行
    fc.switch()
"""

"""
import gevent


def funa(n):
    for i in range(n):
        # 返回当前正在执行的gevent
        print(gevent.getcurrent(), i)
        # gevent无法识别time.sleep需要引入monkey模块(gevent.monkey.patch_all())
        gevent.sleep(1)


if __name__ == '__main__':
    # 创建gevent
    g1 = gevent.spawn(funa, 7)
    g2 = gevent.spawn(funa, 1)
    g3 = gevent.spawn(funa, 3)
    # join是当前gevent执行完就退出了，并不是等所有的gevent执行完毕；
    # 当前gevent执行完之后的其他gevent执行完不会退出
    g3.join()
    # gevent.joinall([g1, g2, g3])
    print("结束了吗")
"""

