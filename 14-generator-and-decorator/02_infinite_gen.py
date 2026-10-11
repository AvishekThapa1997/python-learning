def infinte_gen():
    count = 1
    while True:
        print("Yield Started")
        yield count
        count += 1
        print("Yield End")
        print("=============")

generate = infinte_gen()
 
for _ in range(10):
    print(next(generate))
    print("Yield Received======")        