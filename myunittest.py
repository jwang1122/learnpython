from math import pi


def circle_area(r):
    return pi * (r ** 2)


radius = [2, 0, -3, 2 + 5j, True, "radius"]
message = "Area of circle with r = {radius} is {area}."

for r in radius:
    a = circle_area(r)
    print(message.format(radius=r, area=a))

