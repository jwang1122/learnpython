class Student:
    def __init__(self, name, grade, age):
        self.name = name;
        self.grade =grade;
        self.age = age;

    def __repr__(self):
        return repr((self.name, self.age, self.grade))
#        return "Name: %s" % self.name

students = [Student("John", "A", 15), Student("David", "B", 13), Student("Helen","C", 16)]

print(sorted(students, key=lambda s: s.age))
print(students)
students.sort(key=lambda s: s.age)
print(students)

data = (7,2,4,8,2,87,12,32)
#data.sort()
print(sorted(data))

def s_sort(student):
    return student.age

print(sorted(students, key=s_sort))

from operator import attrgetter
print(sorted(students, key=attrgetter('name')))