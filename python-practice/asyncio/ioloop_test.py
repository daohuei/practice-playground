import asyncio
from tornado.ioloop import IOLoop

loop = asyncio.get_event_loop()
io_loop = BaseAsyncIOLoop(asyncio_loop=loop)


io_loop = IOLoop.current()
print(type(io_loop))