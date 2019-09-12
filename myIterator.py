class MyRange:
    def __init__(self, start, stop):
        self.stop = stop
        self.value = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.value > self.stop:
            raise StopIteration
        current = self.value
        self.value += 1
        return current

    def __repr__(self):
        return str(self.value)

for x in MyRange(1, 10):
    print(x)

x = MyRange(1, 10)
print(help(x))

print(next(x))
print(next(x))
print(next(x))

print("print the MyRange instance:", x)

for y in x:
    print(y)
