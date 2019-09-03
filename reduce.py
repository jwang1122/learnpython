from functools import reduce

data = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

multiplier = lambda x, y: x * y

print(reduce(multiplier, data))

p = 1
for x in data:
    p = p * x

print(p)