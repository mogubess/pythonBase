#並行(Concurrent) Threading
#並列(Parallel) Multiprocess

#コルーチンの理解

#####
# ジェネレータのコルーチン
# def g_hello():
#     while True:
#         r = yield 'hello'
#         yield r
#
# g = g_hello()
# print(next(g))
# print(g.send('mike'))
# print(next(g))
# print(g.send('nancy'))
#--------------------------------
# hello
# mike
# hello
# nancy
#--------------------------------

#####
#yield fromの処理について
#
# def s_hello():
#     yield 'hello 1'
#     yield 'hello 2'
#     yield 'hello 3'
#     return 'done'

# def g_hello():
#     while True:
#         r= yield from s_hello()
#         yield r

# g = g_hello()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))

#--------------------------------
# hello 1
# hello 2
# hello 3
# done
# hello 1
# hello 2
# hello 3
# done
#--------------------------------

#####
#コルーチンとネイティブコルーチン
#
# import asyncio
# import multiprocessing
# import threading
# import time
#
# loop = asyncio.get_event_loop()
#
# #@asyncio.coroutine
# async def worker():
#     print('start')
#     # time.sleep(2)
#     #yield from asyncio.sleep(2) #Ver3.5ぐらいまで @asyncio.coroutine
#     await asyncio.sleep(2) #Ver3.5以降の記載方法 async/await
#     print('stop')
#
# if __name__ == '__main__':
#     loop.run_until_complete(asyncio.wait([worker(),worker()]))
#     loop.close()

#####
# asyncioを使用する場面
# pip install aiohttp==2.3.6
import asyncio
import time
import aiohttp
import requests

loop = asyncio.get_event_loop()

#これだと並列化できていない
# async def hello(url):
#     print(requests.get(url).content)
#     print(time.time())

#ThirParty使っての並列化
async def hello(url):
    # async with aiohttp.ClientSession() as session:
    #     async with session.get(url) as response:
    #         response = await response.read()
    #         print(response)
    #         print(time.time())
    await asyncio.sleep(10)

loop.run_until_complete(asyncio.wait([
    hello("http://httpbin.org/headers"),
    hello("http://httpbin.org/headers")]))
