import asyncio
import types


async def request_server(name):
#    reader, writer = await asyncio.open_connection('127.0.0.1', 8888, loop=loop)
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
    writer.write(name.encode())
    # writer.write_eof()
    await writer.drain()

    data = await reader.read(100)
    data = int(data.decode())
    writer.close()
    await writer.wait_closed()
    return data

# @asyncio.coroutine
# async def request_server(name,loop):
#     yield
#     return 'done'

async def main(name):
    print('chunk reader')
    result = await request_server(name)
    print(result)


asyncio.run(asyncio.wait([
    main('task1'),
    main('task2')
    ]))


# loop.run_until_complete(asyncio.wait([
#     main('task1',loop), main('task2',loop)]))
# loop.close()