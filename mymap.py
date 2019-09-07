temps = [("Berlin", 29),("Cairo", 36),("Buenos Aires", 19),("Los Angeles", 26),("Tokyo", 27),("New York", 28),("London", 22),("Beijing", 32)]
c2f = lambda data: (data[0], round((9 / 5) * data[1] + 32, 2))

x = list(map(c2f, temps))
# x.sort(key=lambda t: t[1])
y = sorted(x, key=lambda t: t[1], reverse=True)
print(y)
print(x)