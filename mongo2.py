from pymongo import MongoClient
import pprint

client = MongoClient("mongodb://localhost:27017")
db = client["huaxia"]
students = db.students

student = {"first_name": "Balaji", "last_name": "Johnson", "grade": "10", "age": 13}

#result = students.insert_one(student)
#if result.acknowledged:
#    print("Course Added. The student Id is", result.inserted_id)

group1 = [
    {"first_name": "Arror", "last_name": "Yu", "grade": "10", "age": 14},
    {"first_name": "Joe", "last_name": "Johnson", "grade": "8", "age": 13},
    {"first_name": "Helen", "last_name": "Martin", "grade": "11", "age": 15},
    {"first_name": "Miky", "last_name": "Johnson", "grade": "7", "age": 12},
    {"first_name": "Macheal", "last_name": "Williams", "grade": "9", "age": 13}
]

# results = students.insert_many(group1)
#for id in results.inserted_ids:
#    print("Student is Added. The Id is", str(id))

students = students.find({
    'last_name':'Johnson'
});
for s in students:
    pprint.pprint(s)

#print(group1)