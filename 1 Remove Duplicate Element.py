# 1. Python Program to Remove Duplicate Element From a List

# list with duplicate numbers
a_list = [10, 20, 20, 10, 10, 30, 20, 10, 50, 60, 40, 80, 50, 40]

duplicates_list = [] # list one
uniques_list = [] # list two

for number in a_list:
    if number not in uniques_list:
        uniques_list.append(number)
    else:
        duplicates_list.append(number)

print(f"Uniques List with duplicate removed: {uniques_list}")
