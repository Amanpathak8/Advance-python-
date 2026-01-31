import asyncio 
import time 

async def process1():
    print("process-1First Step")
    await asyncio.sleep(3)
    print("process-1 Second step")
   
    
async def process2():
    print("process-2 First Step")
    await asyncio.sleep(3)
    print("process-2second step")

async def main():
    
    task = await asyncio.gather(process1(),process2())
    # await (process1())
    # await (process2())
    print("main Completed")


asyncio.run(main())


