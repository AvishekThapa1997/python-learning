import asyncio

users = [
    {
        "id":i,
        "name":f"User {i}"
    }
    for i in range(10)
]
async def get_user(user_id):
    print("Fetching")
    await asyncio.sleep(2)
    user = next((user for user in users if user["id"] == user_id), None)
    return user

async def main():
    result = await asyncio.gather(
        get_user(1),
        get_user(2),
        get_user(100)
    )
    print(result)

asyncio.run(main())    


