# 5. Python Program to Get File Creation and Modification Date

# we will be using the Os and time module from inbuilt python library

import os
import time

# Path to the file/directory
path = r"myfile.txt"

time_at_creation = os.path.getctime(path)
time_at_modification = os.path.getmtime(path)

#convert time in sec to timestamp

creation_time = time.ctime(time_at_creation)
modification_time = time.ctime(time_at_modification)

print(
    f"The file located at the path {path} was created at {creation_time} and was last modified at {modification_time}")