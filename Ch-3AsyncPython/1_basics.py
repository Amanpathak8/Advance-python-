import asyncio 
import time 

async def process1():
    print("process-1First Step")
    asyncio.sleep(6)
    result = await process2()
    print("process-1 Second step")
    print(f"process2 result {result}")
    
async def process2():
    print("process-2 First Step")
    await asyncio.sleep(9) 
    print("process-2second step")
    print("process-2 completed")
    
asyncio.run(process1())

