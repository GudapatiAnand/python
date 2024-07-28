#Python: Get the current Time method 1

# import datetime

# print(datetime.datetime.now().time())

#method 2

from datetime import datetime

current_time=datetime.now().strftime("%H:%M:%S")

print("Current Time:",current_time)