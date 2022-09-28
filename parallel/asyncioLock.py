#ドキュメントのプリミティブを参照(ドキュメントは古いままな2022/09/27)
# https://man.plustar.jp/python/library/asyncio-sync.html


# Worker1でLockを取得して、Sleepを抜けたら、Woker2でLockを取得する
import asyncio

loop = asyncio.get_event_loop()

async def worker1(lock):
    print('worker1 start')
    async with lock:
        print('worker1 get lock')
        await asyncio.sleep(3)
    print('worker1 end')

async def worker2(lock):
    print('worker2 start')
    async with lock:
        print('worker2 get lock')
        await asyncio.sleep(3)
    print('worker2 end')

mlock = asyncio.Lock()
loop.run_until_complete(asyncio.wait([
    worker1(mlock),worker2(mlock)
]))
loop.close()
