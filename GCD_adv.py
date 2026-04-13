# Find the GCD of two numbers. GCD is always non-negative

# Euclidean Algorithm

# GCD(a,b) = GCD(b,a%b)

a = int(input("Enter first number: "))
b = int(input("Enter Second Number: "))

# gcd(12,6) = gcd(6,12%6)

def GCD(a:int,b:int)->int:
    while b!=0:           #as per the algo, loop will stop when b becomes 0 and we return a
        a,b = b,a%b
    return a

print(GCD(a,b))