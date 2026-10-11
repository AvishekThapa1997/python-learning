nums = [1,[2,3],4,5]
square_nums = [num * num for num in nums if isinstance(num, list) for num in num]
print(square_nums) 