def gen_even_numbers():
    num = 2
    while num < 100:
        yield num
        num += 2

def gen_odd_numbers():
    num = 1
    while num < 100:
        yield num
        num += 2


def gen_numbers():
    yield from gen_even_numbers()
    yield from gen_odd_numbers()

numbers = gen_numbers()

for num in numbers:
    print(num)
    if num > 50:
        numbers.close()
        print("Generator Closed")