#Write a Python program that calculates the sum of odd and even numbers in a tuple, then refactor it using any AI tool.

# Original Version: Calculate the sum of odd and even numbers in a tuple

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

even_sum = 0
odd_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)

# Refactored Version (using list comprehensions)

even_sum_refactored = sum(num for num in numbers if num % 2 == 0)
odd_sum_refactored = sum(num for num in numbers if num % 2 != 0)

print("Refactored - Sum of even numbers:", even_sum_refactored)
print("Refactored - Sum of odd numbers:", odd_sum_refactored)


