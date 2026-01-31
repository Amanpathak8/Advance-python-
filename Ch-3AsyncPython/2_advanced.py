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
    # asyncio.gather runs process1() AND process2() CONCURRENTLY (at same time)
    # It waits until BOTH are finished
    # Timeline:
    #   - process1 first step
    #   - process2 first step
    #   - both sleep 3 seconds together
    #   - both print second step
    #   - then main continues
  
    print("main Completed")


asyncio.run(main())


