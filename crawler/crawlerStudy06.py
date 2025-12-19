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
"""

"""
import asyncio
import aiohttp
import aiofiles
import json
import requests
import time

# 1. 增加信号量，限制同时只有10个请求在跑
sem = asyncio.Semaphore(10)
async def download(session, bookId, chaptid, par_file_path, headers):
    url = f"https://apibi.cc/api/chapter?id={bookId}&chapterid={chaptid}"
    # 使用信号量控制并发
    async with sem:
        try:
            async with session.get(url, ssl=False, headers=headers, timeout=10) as resp:
                text = await resp.text()
                json_resp = json.loads(text)
                chaptername = json_resp.get("chaptername", f"Unknown_{chaptid}")
                conetext = json_resp.get("txt", "")

                # 移除非法字符，防止文件名导致保存失败
                chaptername = "".join(i for i in chaptername if i not in r'\/:*?"<>|')
                file_path = f"{par_file_path}{chaptername}.txt"

                async with aiofiles.open(file_path, mode='w', encoding='utf-8') as f:
                    await f.write(conetext)
                    print(f"{chaptername} 写入完成")
        except Exception as e:
            print(f"{chaptername}下载失败: {e}")


async def get_chapterid(url, bookId, headers):
    # 这里建议也改成异步获取，或者保留requests但要注意超时
    resp = requests.get(url, verify=False, headers=headers)
    chapter_id = int(resp.json().get("lastchapterid"))
    par_file_path = "./resource/txt/"

    # 2. 在外层统一创建一个 session
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(1, chapter_id + 1):
            tasks.append(asyncio.create_task(download(session, bookId, i, par_file_path, headers)))

        # 使用 wait 等待所有任务
        await asyncio.wait(tasks)


if __name__ == '__main__':
    # 确保文件夹存在
    import os

    if not os.path.exists("./resource/txt/"):
        os.makedirs("./resource/txt/")

    book_id = '2530'
    url = f"https://apibi.cc/api/book?id={book_id}"
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36",
    }
    t1 = time.time()
    asyncio.run(get_chapterid(url, book_id, headers))
    t2 = time.time()
    print("总耗时：", t2 - t1)
"""

import asyncio
import aiohttp
import aiofiles
import json
import requests
import time
import os

# 1. 提高并发数到 100
sem = asyncio.Semaphore(100)


async def download(session, bookId, chaptid, par_file_path, headers):
    url = f"https://apibi.cc/api/chapter?id={bookId}&chapterid={chaptid}"

    # --- 第一阶段：受限的高并发网络请求 ---
    try:
        async with sem:
            # 增加 timeout 防止个别请求卡死整体速度
            async with session.get(url, ssl=False, headers=headers, timeout=15) as resp:
                # 使用 read() 绕过 aiohttp 自动检测编码的耗时过程
                content = await resp.read()
    except Exception as e:
        print(f"章节 {chaptid} 请求失败: {e}")
        return

    # --- 第二阶段：不受限的数据处理与磁盘 IO ---
    # 此时已经释放了信号量“坑位”，其他请求可以立刻补上
    try:
        data = json.loads(content.decode('utf-8'))
        chaptername = data.get("chaptername", f"Unknown_{chaptid}")
        conetext = data.get("txt", "")

        # 快速清理文件名
        clean_name = "".join(i for i in chaptername if i not in r'\/:*?"<>|')
        file_path = os.path.join(par_file_path, f"{clean_name}.txt")

        async with aiofiles.open(file_path, mode='w', encoding='utf-8') as f:
            await f.write(conetext)
    except Exception as e:
        pass  # 忽略部分解析失败，保证整体速度


async def get_chapterid(url, bookId, headers):
    resp = requests.get(url, verify=False, headers=headers)
    chapter_id = int(resp.json().get("lastchapterid"))
    par_file_path = "./resource/txt/"

    # 2. 配置 TCP 连接池，允许更高的并发连接
    connector = aiohttp.TCPConnector(limit=200, use_dns_cache=True)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [
            asyncio.create_task(download(session, bookId, i, par_file_path, headers))
            for i in range(1, chapter_id + 1)
        ]
        await asyncio.gather(*tasks)  # gather 通常比 wait 在处理大量任务时稍微高效


if __name__ == '__main__':
    path = "./resource/txt/"
    if not os.path.exists(path): os.makedirs(path)

    book_id = '88378'
    api_url = f"https://apibi.cc/api/book?id={book_id}"
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36..."}

    t1 = time.time()
    asyncio.run(get_chapterid(api_url, book_id, headers))
    print(f"总耗时：{time.time() - t1:.2f} 秒")
