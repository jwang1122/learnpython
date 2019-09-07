class Student:
    first_name = ""
    last_name = ""
    age = 0

    def __init__(self, firstname, lastname, age):
        self.first_name = firstname
        self.last_name = lastname
        self.age = age

    def findByAge(age, students=[]):
        return filter(lambda s: s.age=age, students)


 students = [Student("john","wang",13), Student("arron","li", 14)]       
 print(filter(lambda s: s.age = 13, students))
