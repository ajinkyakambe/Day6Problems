# 3. Python Program to Capitalize the First Character of a String

# using slicing,upper and lower

def capitalize_string(string):
    final_string = string[0].upper() + string[1:].lower()
    print("String after Capitalize the First Character::")
    print(final_string)


# Driving code
str = "we Can use The inbuilt Method to Perform This task"
capitalize_string(str)
