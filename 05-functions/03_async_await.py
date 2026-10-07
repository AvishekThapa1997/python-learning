import asyncio


async def fetch_data():
    return "data"


async def main():
    result = await fetch_data()
    print(result)


asyncio.run(main())