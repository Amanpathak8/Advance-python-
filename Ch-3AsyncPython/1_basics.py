import asyncio 
import time 

async def process1(): # async means this function returns a coroutine and can be awaited by the event loop
    print("process-1First Step")
    asyncio.sleep(6)
    result = await process2() #await is needed to pause without blocking resources so process 2 can start process 2 first step 
    print("process-1 Second step")
    print(f"process2 result {result}")
    
async def process2():
    print("process-2 First Step")
    await asyncio.sleep(9) 
    print("process-2second step")
    print("process-2 completed")
    
asyncio.run(process1())

