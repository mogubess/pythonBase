#WIndowsだとwarnigがでます。
import asyncio
import time
import concurrent.futures

loop = asyncio.get_event_loop()

def blocking_task(name):
    print('block {}'.format(name))
    time.sleep(1)
    return 'done {}'.format(name)

async def main(name, loop):
    def done_callback(future):
        print(future.result())

    executor = concurrent.futures.ProcessPoolExecutor(max_workers=5)
    for i in range(4):
        print(i)
        future = loop.run_in_executor(executor, blocking_task, name)
        future.add_done_callback(done_callback)
    executor.shutdown(wait=True)

from multiprocessing import freeze_support
if __name__ == '__main__':
    print('start freeze suport')
    freeze_support()

loop.run_until_complete(asyncio.wait([main('task1',loop),main('task2',loop)]))
loop.close()

