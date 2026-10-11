def serve():
    yield 1
    yield 2
    yield 3

gen = serve()
for num in gen:
    print(num)

    