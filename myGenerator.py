def my_range(start, end):
    current = start
    while current <= end:
        yield current
        current += 1


for x in my_range(1, 10):
    print("in for loop: ", x)

nums = my_range(1, 10)

print(next(nums))
print(next(nums))

# redefine function will not cause any issue
# be careful, you don't want to do for loop on this one!!!
def my_range(start):
    current = start
    while True:
        yield current
        current += 1


nums = my_range(1)

print("infinite: ", next(nums))
print("infinite: ", next(nums))


def calc_square(numbers):
    result = []
    for number in numbers:
        result.append(number * number)
    return result


data = [1, 2, 3, 4, 5]
print(calc_square(data))


def calc_square(numbers):
    for number in numbers:
        yield number ** 2


data = [1, 2, 3, 4, 5]
print(calc_square(data))

square = calc_square(data)
try:
    print(next(square))
    print(next(square))
    print(next(square))
    print(next(square))
    print(next(square))
    print(next(square))
    print(next(square))
except StopIteration:
    pass

squares = (x*x for x in [1,2,3,4,5])
print(squares)
l = list(squares)
print(list(squares)) # the squares is already loop through.
for x in squares:
    print("generator: ", x)

for x in l:
    print("x: ", x)
