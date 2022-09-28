import asyncio

loop = asyncio.get_event_loop()

#タスクを起動して、結果を戻す処理(set_result->result)
async def f(future):
    await asyncio.sleep(1)
    future.set_result('Future is done!')

future = asyncio.Future()
asyncio.ensure_future(f(future))
loop.run_until_complete(future)
print(future.result())
loop.close()

#コールバック処理を呼び出す場合
#run_until_complete()で停止するのではなく、run_foreverでタスクを回し、コールバックで、stopして、結果を受け取る
async def f(future):
    await asyncio.sleep(1)
    future.set_result('Future is done!')

def got_result(future):
    print(future.result())
    loop.stop()

future = asyncio.Future()
asyncio.ensure_future(f(future))

future.add_done_callback(got_result)

loop.run_forever()
loop.close()

