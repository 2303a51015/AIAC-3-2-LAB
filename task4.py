'''
generate a python code to convert binary number to decimal
'''
def binary_to_decimal(binary_str):
    decimal_value = 0
    binary_str = binary_str[::-1]  # Reverse the string to process from least significant bit
    for index, digit in enumerate(binary_str):
        if digit == '1':
            decimal_value += 2 ** index
    return decimal_value
# Example usage
binary_input = input("Enter a binary number: ")
decimal_output = binary_to_decimal(binary_input)
print(f"The decimal value of binary {binary_input} is {decimal_output}.")
