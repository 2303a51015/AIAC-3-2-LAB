# generate an iterative factorial program using a loop include comments and meaningful variable names
def factorial_iterative(number):
    # Calculates factorial using an iterative approach (loop)
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result
# generate a recursive factorial program
# ensure it returns the same output as the iterative version

def factorial_recursive(number):
    # Calculates factorial using a recursive approach
    if number < 0:
        return "Factorial is not defined for negative numbers"
    if number in (0, 1):
        return 1
    return number * factorial_recursive(number - 1)
# write main code to call both functions and display their results
num = int(input("Enter a number to calculate its factorial: "))
iterative_result = factorial_iterative(num)
recursive_result = factorial_recursive(num)
print(f"Iterative: The factorial of {num} is {iterative_result}")
print(f"Recursive: The factorial of {num} is {recursive_result}")
