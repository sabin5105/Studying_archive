import asyncio

async def make_americano():
    print("start americano")
    await asyncio.sleep(3)
    print("end americano")

async def make_latte():
    print("start latte")
    await asyncio.sleep(5)
    print("end latte")

async def main():
    coro1 = make_americano()
    coro2 = make_latte()
    await asyncio.gather(coro1,coro2)

print("main start")
asyncio.run(main())
print("main end")