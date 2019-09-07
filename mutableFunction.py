# def add_employee(employee, employeeList=[]):  # causes problem, add to list even you don't pass the list.
#     # def add_employee(employee, employeeList=None):
#     #     if(employeeList==None):
#     #         employeeList=[]
#     employeeList.append(employee)
#     print(employeeList)


# employees = ["ailian", "charles"]
# employee1 = "john"
# add_employee(employee1, employees)
# add_employee("Paul")
# employee2 = "david"
# add_employee(employee2)
# newlist=[]
# add_employee("Arron", newlist)
# add_employee("Martin")

# def add(a, b=6):
#     return a + b

# print(add( 3,5))
# print(add(3))
# print(add(4))
from datetime import datetime
import time

#def display_time(mytime = datetime.now()):
def display_time(mytime = None):
    if mytime is None:
        mytime = datetime.now()
    print(mytime.strftime('%B, %d, %Y %H:%M:%S'))

display_time()
time.sleep(2)
display_time()
time.sleep(2)
display_time()
time.sleep(2)
display_time()
