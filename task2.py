'''
n=12
m= 18
diaplay GCD of n and m as 6
'''
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
n = 12
m = 18
print("GCD of", n, "and", m, "is", gcd(n, m))
