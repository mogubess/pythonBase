import asyncio
import collections

class CountServer(object):
    def __init__(self) -> None:
        self.counter = collections.Counter()
        self.lock = asyncio.Lock()

    async def handle_echo(self, reader,writer):
        data = await reader.read(100)
        name = data.decode()

        async with self.lock:
            if self.counter[name] > 10:
                writer.write(b'-1')
                self.counter[name] = 0
            else:
                writer.write(str(self.counter[name]).encode())
                self.counter[name] +=1
        await writer.drain()
        writer.close()

async def main():
    count_server = CountServer()
    coro = await asyncio.start_server(count_server.handle_echo, '127.0.0.1', 8888)

    addrs = ', '.join(str(sock.getsockname()) for sock in coro.sockets)
    print(f'Serving on {addrs}')

    async with coro:
        await coro.serve_forever()

asyncio.run(main())
# # server = loop.run_until_complete(coro)
# loop = asyncio.get_event_loop()
# print('server: {}'.format(server.sockets[0].getsockname()))
# try:
#     loop.run_forever()
# except KeyboardInterrupt:
#     pass

# server.close()
# loop.run_until_complete(server.wait_closed())
# loop.close()
