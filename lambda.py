from math import pi


def f(x):
    return 3 * x + 1


x = 5
# print("3 X %d + 1 = %d" % (x, f(x)))

g = lambda x: 3 * x + 1

print(g(5))

y = 6


h = lambda x, y: 3 * x + 5 * y + 10

print(h(x, y))

radii = [2, 1.4, 4.3, 2.5]
print(list(map(lambda r: round(pi * r ** 2, 2), radii)))

scifi_authors = ["Isaac Asimov", "Rray Bradbury","Robert Heinlein","Arthus C. Clarke","Frank Herbert","Orson Scott Card", "Douglas Adams","H. G. Wells", "Leigh Brackeet"]
scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())
print(scifi_authors)

data = [12,32,53,21,111,13,31]
data.sort()
print(data)
data.sort(key=lambda d: str(d))
print(data)