data = [12,32,53,21,111]
data.sort() # Sort in ascending order
print(data)
data.sort(reverse=True) # Sort in descending order
print(data)

print(sorted(data))
print(sorted("This is a test string from John".split(), key=str.lower))

students = [("John", "B", 15), ("Arron", "A", 12), ("David", "C", 11)] # student tuple
print(sorted(students, key=lambda s: s[0])) # Sort by student name

age = lambda student: student[2]
print(sorted(students, key=age))