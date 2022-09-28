# Worker1でLockを取得して、Sleepを抜けたら、Woker2でLockを取得する
import asyncio
from msilib.schema import Condition

loop = asyncio.get_event_loop()

async def worker1(condition):
    print('worker1 prestart')    
    async with condition:
        print('worker1 waitstart')    
        await condition.wait()
        print('worker1 start')
        print('worker1 get condition')
        await asyncio.sleep(3)
        print('worker1 end')

async def worker2(condition):
    print('worker2 prestart')    
    async with condition:
        print('worker2 waitstart')    
        await condition.wait()
        print('worker2 start')
        print('worker2 get condition')
        await asyncio.sleep(3)
        print('worker2 end')

async def worker3(condition):
    print('worker3 prestart')    
    # await asyncio.sleep(1) #worker1/2がwaitする前に、notifyallしてしまうのを避けるため
    async with condition:
        print('worker3 start')
        await asyncio.sleep(3)
        print('worker3 end')
        condition.notify_all()

condition = asyncio.Condition()
loop.run_until_complete(asyncio.wait([
    worker1(condition),worker2(condition),worker3(condition)
]))
loop.close()
