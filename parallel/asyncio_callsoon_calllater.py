import asyncio

loop = asyncio.get_event_loop()


def hello(name,loop):
    print('Hello {}'.format(name))
    loop.stop()

#3秒後に登録関数を発火させる
loop.call_later(3,hello,'Mike',loop)
#即実行
loop.call_soon(hello, 'Nancy', loop)
loop.run_forever()
loop.close()
