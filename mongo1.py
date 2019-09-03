from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client['test-database']
courses = db.cursors

course = {
    'author':'Balaji',
    'course':'MongoDB Tutorial',
    'price':100,
    'rating':5
}

arr_courses = [
  {
    'author':'Balaji',
    'course':'MongoDB Tutorial',
    'price':100,
    'rating':5
},
{
    'author':'John Wang',
    'course':'Java Tutorial',
    'price':100,
    'rating':9
} ,
{
    'author':'Charles',
    'course':'SQL Tutorial',
    'price':130,
    'rating':8
},
{
    'author':'Weiping',
    'course':'Python Tutorial',
    'price':120,
    'rating':7
} 
]

#results = courses.insert_many(arr_courses)
#for id in results.inserted_ids:
#    print("Course Added. The course Id is", str(id))

#result = courses.insert_one(course)
#if result.acknowledged:
#    print("Course Added. The course Id is", result.inserted_id)