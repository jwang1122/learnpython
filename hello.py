from datetime import date

name = "John Wang"
print("Hello,", name)
print("Hello, %s!" % name)
print("Hello, {0}!".format(name))

today = date.today()
print(f"Today is {today}. Hello, {name}!")
print("Today is {1}. Hello, {0}!".format(name, today))
print("Hello, %s. Today is %s." % (name, today))
msg = (name, today)
print("Hello, %s. Today is %s." % msg)
