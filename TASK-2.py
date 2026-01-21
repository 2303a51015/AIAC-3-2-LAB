# optimize this code, reduce unnecessary variables,
# simplify logic, and improve readability
def factorial(n):
     if n < 0:
         raise ValueError("Factorial is not defined for negative numbers")
     elif n == 0 or n == 1:
         return 1
     else:
            result = 1
            for i in range(2, n + 1):
                result *= i
            return result
        else:
            raise ValueError("Input must be a non-negative integer")    
            else:   
        n = int(input("Enter a non-negative integer: "))
        if n < 0:
            print("Factorial is not defined for negative numbers")
        else:
            result = 1
            for i in range(2, n + 1):
                result *= i
            print(f"The factorial of {n} is {result}")
            
            return result