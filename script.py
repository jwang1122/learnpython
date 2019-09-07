import sys
from math import pi, sin
import requests

print(sys.version)
print(sys.executable)
count = 0
while True:
    count += 1
    print(count)
    if count >= 5:
        break

r = requests.get("https://www.google.com")
print(r.status_code)

import calc

print(calc.add(3, 5))
print(calc.add(3 + 5j, 6 + 2j))
print(calc.add("4", "5"))

nums = [11,30,44,54]
print(list(map(lambda n: n**2, nums)))

nums = (2, 4, 6, 8)
print(list(map(lambda r: pi*r**2, nums)))

rads = ()
