'''
a=18
display as harshad number if it is  or not a harshad number
b=21
display as harshad number if it is  or not a harshad number
c=19
display as harshad number if it is  or not a harshad number
'''
def is_harshad_number(num):
    digit_sum = sum(int(digit) for digit in str(num))
    return num % digit_sum == 0
numbers = [18, 21, 19]
for number in numbers:
    if is_harshad_number(number):
        print(f"{number} is a Harshad number.")
    else:
        print(f"{number} is not a Harshad number.")
        