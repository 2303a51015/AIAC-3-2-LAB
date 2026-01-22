'''
n,m=4,6
display LCM as 12
a,b=5,10
display LCM as  10
c,b=    7,3
display LCM as 21
'''
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
def lcm(x, y):
    return x * y // gcd(x, y)
pairs = [(4, 6), (5, 10), (7, 3)]
for x, y in pairs:
    print("LCM of", x, "and", y, "is", lcm(x, y))
    