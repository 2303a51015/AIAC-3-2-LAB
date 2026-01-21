# write a python program to calculate factorial using a user-defined function
# use meaningful variable names and add inline comments
def calculate_factorial(number):
    # This function calculates the factorial of a given number
    if number < 0:
        return None

    result = 1
    for i in range(2, number + 1):
        result *= i
    return result


# Main execution block
num = int(input("Enter a number: "))

factorial_result = calculate_factorial(num)

if factorial_result is None:
    print("Factorial does not exist for negative numbers")
else:
    print(f"Factorial of {num} is {factorial_result}")
