
#what is concurrent programming
#asynchronous programming
# ascyncio

#pro topic

import asyncio
import time
async def fun1():
    print('start fun1')
    await asyncio.sleep(1)
    print('end fun1')

async def fun2():
    print('start fun2')
    await asyncio.sleep(1)
    print(
        'end fun2'
    )

#event loop
#coroutine
#blocking code
async def main():
    # await fun1()
    # await fun2()
    await asyncio.gather(fun1(),fun2())
asyncio.run(main())