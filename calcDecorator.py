import time


def calc_square(numbers):
    start = time.time()
    result = []
    for number in numbers:
        result.append(number ** 2)
    end = time.time()
    print("calc_squqre took %s milliseconds." % str((end - start) * 1000))
    return result


def calc_cube(numbers):
    result = []
    for number in numbers:
        result.append(number ** 3)
    return result


array = range(1, 100000)
out_square = calc_square(array)
out_cube = calc_cube(array)
# print(out_square)
# print(out_cube)
