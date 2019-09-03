def myage(birthYear):
    thisYear = 2019
    age = (thisYear - birthYear)
    print('My age is ',  age)
    return age

myage(2005)


from datetime import date
today = date.today()
print(today)
print(today.year)
