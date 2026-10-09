from .utils import user_util

def get_user():
    return user_util.format_user({
        "name":"Avishek Thapa",
        "age": 30
    })