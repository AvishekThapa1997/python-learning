import copy

original = [[1, 2], [3, 4]]

# shallow = original[:]
shallow = copy.copy(original)
deep = copy.deepcopy(original)

shallow[0][0] = 100
deep[1][0] = 200

print(original)
print(shallow)
print(deep)