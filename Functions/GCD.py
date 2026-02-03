def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#output:
result = gcd(24, 18)
print(result)
