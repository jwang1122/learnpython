from datetime import date


class User:
    def __init__(self, full_name, birthday):
        self.full_name = full_name

        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[1]

        yyyy = int(birthday[0:4])
        mm = int(birthday[4:6])
        dd = int(birthday[6:8])
        self.birthday = date(yyyy, mm, dd)

        age_in_days = (date.today() - self.birthday).days
        self.age = int(age_in_days / 365)
    def __repr__(self):
        return repr(f"{self.full_name} ({self.age})")

user1 = User("John Wang", "20010901")
print(user1)
print(user1.full_name)
print(user1.birthday)
print(user1.first_name, user1.last_name)

print(user1.age, "years old.")

user2 = User("Arron Wang", "20050901")
print(user2)