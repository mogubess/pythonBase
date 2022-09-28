#ドキュメントのプリミティブを参照(ドキュメントは古いままな2022/09/27)
# https://man.plustar.jp/python/library/asyncio-sync.html


# Worker1でLockを取得して、Sleepを抜けたら、Woker2でLockを取得する
import asyncio

loop = asyncio.get_event_loop()

async def worker1(event):
    print('worker1 start')
    await event.wait()
    print('worker1 get event')
    await asyncio.sleep(3)
    print('worker1 end')

async def worker2(event):
    print('worker2 start')
    await event.wait()
    print('worker2 get event')
    await asyncio.sleep(3)
    print('worker2 end')

async def worker3(event):
    print('worker3 start')
    print('worker3 get event')
    await asyncio.sleep(3)
    print('worker3 end')
    event.set()

event = asyncio.Event()
loop.run_until_complete(asyncio.wait([
    worker1(event),worker2(event),worker3(event)
]))
loop.close()
