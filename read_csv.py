# read_csv.py

import pandas as pd
#from datetime import datetime
import matplotlib.pyplot as plt

# import matplotlib.dates as mdates

mydata = pd.read_csv("student.csv")
# print(mydata)

# mydata['FirsName'] = mydata['#'].map(lambda x: str(x))
# mydata['Score'] = mydata['Score'].map(lambda x: str(x))

#x = mydata["First Name"]
#y = mydata["Score"]

# plot
plt.plot(mydata["First Name"], mydata["Score"])
# plt.gcf().autofmt_xdate()

plt.show()
# print(y)

