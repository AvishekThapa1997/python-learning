import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


def check_stock(item):
    print(f"Checking {item} stock")
    time.sleep(3) # Blocking 
    return f"{item} stock: 42"


async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        await loop.run_in_executor(pool, check_stock, "Shoe")   


asyncio.run(main())
print("Main completed")

