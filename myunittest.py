from circle import circle_area

radius = [2, 0, -3, 2 + 5j, True, "radius"]
message = "Area of circle with r = {radius} is {area}."

for r in radius:
    a = circle_area(r)
    print(message.format(radius=r, area=a))

