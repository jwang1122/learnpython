import statistics

data = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]
avg = statistics.mean(data)
print("The average of the data list is %.3f." % avg)

print("The data above average are ", list(filter(lambda x: x > avg, data)))

countries = [
    "",
    "Argentina",
    "Brazil",
    "Chile",
    "",
    "Colombia",
    "",
    None,
    "Ecuador",
    "China",
    "Venezuela",
]
print(list(filter(None, countries)))

