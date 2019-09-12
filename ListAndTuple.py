# list: square braces, in sequence
# tuple: rounded braces, immutable, run faster, in sequence
# set: curly braces, random order
# dictionary: curly braces, key-value pair separated by ':'

list1 = ["computer", "TV", "camara", "printer"]
del list1[1]
print(list(map(lambda w: w.title(), list1)))

list2 = ["string", 2, 4, "number"]
for x in list2:
    print(x, end="; ")
print()

print(list2)

list2[1] = "john"
print(list2)

tuple1 = ("string", 2, 4, "number")
print(tuple1)
# tuple1[2] = "john"
# print(tuple1)

set1 = set(["computer", "TV", "camera", "printer"])  # __init__ by iterable
print(set1)
set2 = {"computer", "TV", "camera", "printer", 2, 5}
print(set2)

dic1 = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",    6: "Saturday",
    7: "Sunday",
}
print(dic1)
del dic1[4]
print(dic1)
dic1[4]='Thursday'
print(dic1)

print(dic1[3])
print(dic1.get(6))
phonebook=dict()
phonebook={}
phonebook["john"] = 2818182512
phonebook["ailian"] = 8326603968
print(phonebook)
phonebook=dict({"john":123456789, "charles":987654321, "ailian":488452345})
print(phonebook)