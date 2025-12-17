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
"""


import requests
import asyncio
import aiohttp
import aiofiles
import json
import time

async def get_chapterid(url, bookId, headers):
    resp = requests.get(url, verify=False, headers=headers)
    chapter_id = int(resp.json().get("lastchapterid"))
    par_file_path = "./resource/txt/"
    tasks = []
    for i in range(1, chapter_id + 1):
        tasks.append(asyncio.create_task(download(bookId, i, par_file_path, headers)))
    await asyncio.wait(tasks)


async def download(bookId, chaptid, par_file_path, headers):
    url = f"https://apibi.cc/api/chapter?id={bookId}&chapterid={chaptid}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False, headers=headers) as resp:
            text = await resp.text()
            json_resp = json.loads(text)
            chaptername = json_resp["chaptername"]
            conetext = json_resp["txt"]
            file_path = par_file_path + chaptername + ".txt"
            async with aiofiles.open(file_path, mode='w', encoding='utf-8') as f:
                await f.write(conetext)
                print(chaptername, "write over")


if __name__ == '__main__':
    book_id = '2530'
    url = f"https://apibi.cc/api/book?id={book_id}"
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/142.0.0.0 "
                      "Safari/537.36",
        'Connection': 'close'
    }
    t1 = time.time()
    asyncio.run(get_chapterid(url, book_id, headers))
    t2 = time.time()
    print("耗时间：",t2-t1)

