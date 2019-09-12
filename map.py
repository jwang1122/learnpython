from math import pi


def area(r):
    """Return area of a circle with radius 'r'."""
    return round(pi * (r ** 2), 2)


r = 4
print("The circle area for radius={0} is {1:.2f}".format(r, area(r)))

radius = [2, 1.4, 4.3, 2.5] # List

#areas = []

#for r in radius:
#    areas.append(area(r))
#print(areas)

for x in map(area, radius):
    print(x)
    
print(list(map(area, radius)))

radii = (2.3, 1.3, 4.2, 1.7) # Tuple
print(list(map(lambda r: pi*r**2, radii)))