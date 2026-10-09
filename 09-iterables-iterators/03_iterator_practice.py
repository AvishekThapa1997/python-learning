def read_batches(item , batch):
    pos = 0
    while pos < len(item):
        start = pos # 0
        end = pos + batch # 0 + 3 = 3
        yield item[start:end]
        pos = end
       

items = [1, 2, 3, 4, 5, 6, 7]
for batch in read_batches(items, 3):
    print(batch)        