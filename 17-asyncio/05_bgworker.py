import asyncio
import threading
import time


def background_worker():
    while True:
        time.sleep(2)
        print("Loggin the system health")

async def fetch_orders():
    await asyncio.sleep(7)
    print("Orders fetched")


threading.Thread(target=background_worker, daemon=True).start()

asyncio.run(fetch_orders())    