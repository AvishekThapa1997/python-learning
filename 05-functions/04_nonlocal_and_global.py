global_value = 10
def outer(n):
    if isinstance(n, int):
        outer_val = 20
    def inner():
        def inner_inner():
            global global_value
            nonlocal outer_val
            print(outer_val)
            global_value = 50
        inner_inner()
    inner()
    print(outer_val)

outer(2)  
print(global_value)  

