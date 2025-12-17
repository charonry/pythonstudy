"""
import asyncio
import time


async def func1():
    print("hello 异步协程一")
    # 当程序出现了同步操作的时候，异步就中断
    # time.sleep(3)
    # 异步操作
    await asyncio.sleep(3)
    print("hello 异步协程一")


async def func2():
    print("hello 异步协程二")
    # time.sleep(2)
    # 异步操作
    await asyncio.sleep(2)
    print("hello 异步协程二")


async def finalfunc():
    tasks = [asyncio.create_task(func1()), asyncio.create_task(func2())]
    await asyncio.wait(tasks)


if __name__ == "__main__":
    t1 = time.time()
    asyncio.run(finalfunc())
    t2 = time.time()
    print(t2 - t1)
"""

import asyncio
import aiohttp

urls = [
    "https://biizhi.com/wp-content/uploads/2025/10/20251026141001-68fe2bb9270a0-1536x864.jpg",
    "https://biizhi.com/wp-content/uploads/2025/10/20251026140957-68fe2bb5492f0-1536x864.jpg",
    "https://biizhi.com/wp-content/uploads/2025/10/20251026140954-68fe2bb229a04-1536x864.jpg"
]



par_file_path = "./resource/picture/"

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 "
                  "Safari/537.36"
}


async def aiodownload(url):
    name = url.rsplit("/", 1)[1]
    # 异步协程中 with前面必须加上async
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False, headers=headers) as resp:
            file_path = par_file_path + name
            with open(file_path, 'wb') as f:
                # 读取内容是异步，需要await挂起
                f.write(await resp.content.read())
    print(name, "over")


async def asyncfinal():
    tasks = []
    for url in urls:
        task = asyncio.create_task(aiodownload(url))
        tasks.append(task)
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(asyncfinal())
    print("all over!")
