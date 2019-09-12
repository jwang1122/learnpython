def myfunction(what_to_do, data):
    return list(map(what_to_do, data))

data = ["john","charles","ailian"]
x = myfunction(lambda w: w.title(), data)
print(x)
y = myfunction(lambda w: w.upper(), data)
print(y)

data2 = [56,76,86,59]
from circle import circle_area
z = myfunction(circle_area, data2)
print(z)