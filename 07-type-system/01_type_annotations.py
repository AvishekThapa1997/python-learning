# def add(a: int, b: int) -> int:
#     return a + b


# result = add("10", "20")
# print(result)

# def get_users() -> list[str]:
#     return ["User1","User2"]

def get_users() -> dict[int, dict[str,str]]:
    return {
       1:{
            "name":"User-1"
       },
        2:{
            "name":"User-2"
        }
    }

print(get_users())    