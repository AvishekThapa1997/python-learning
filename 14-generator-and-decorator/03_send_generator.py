def gen_square():
    num = yield
    while True:
        num = yield
        yield num * num


sq = gen_square()
next(sq)
for i in range(10):
    print("I", i)
    print(sq.send(i))