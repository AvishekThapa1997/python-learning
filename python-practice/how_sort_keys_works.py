numbers = [4, 1, 7, 2]

# How `key` works in sorted():
# 1. The key function calculates a sorting key for each original element.
# 2. Python sorts those keys in ascending order by default.
# 3. Python returns the original elements in the order determined by their keys.
#
# Example with key=lambda x: -x:
# Original values:  [4,  1,  7,  2]
# Calculated keys: [-4, -1, -7, -2]
# Sorted keys:     [-7, -4, -2, -1]
# Result:          [ 7,  4,  2,  1]
#
# Why descending order?
# Because -7 < -4 < -2 < -1, ascending sorting of the negative keys
# produces descending order of the original positive numbers.

result = sorted(numbers, key=lambda x: -x)

print(result)  # [7, 4, 2, 1]