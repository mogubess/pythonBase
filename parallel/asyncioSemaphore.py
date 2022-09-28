#ドキュメントのプリミティブを参照(ドキュメントは古いままな2022/09/27)
# https://man.plustar.jp/python/library/asyncio-sync.html


# Worker1でLockを取得して、Sleepを抜けたら、Woker2でLockを取得する
import asyncio

loop = asyncio.get_event_loop()

async def worker1(semaphore):
    print('worker1 start')
    async with semaphore:
        print('worker1 get semaphore')
        await asyncio.sleep(3)
    print('worker1 end')

async def worker2(semaphore):
    print('worker2 start')
    async with semaphore:
        print('worker2 get semaphore')
        await asyncio.sleep(3)
    print('worker2 end')

#リソースの数を引数にする、2ならば2つ同時並行
semaphore = asyncio.Semaphore(2)
loop.run_until_complete(asyncio.wait([
    worker1(semaphore),worker2(semaphore)
]))
loop.close()
