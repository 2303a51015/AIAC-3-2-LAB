'''
a=10
display value a's binary representation

'''
def to_binary(n):
    return bin(n).replace("0b", "")
a = 10
print("Binary representation of", a, "is", to_binary(a))
