# 4. Python Program to Count the Number of Digits Present In a Number

def count_digit_in_number(digit):
    count = 0
    while digit > 0:
        digit = digit // 10
        count = count + 1
    print("\n Number of Digits in a Given Number = %d" % count)

# driving code

count_digit_in_number(1234)
count_digit_in_number(44534534)