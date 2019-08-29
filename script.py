import sys
import requests

print(sys.version)
print(sys.executable)
count = 0
while True:
    test = "5"
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
