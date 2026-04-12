# 1. Reverse Digits which handle negative

num = int(input("Enter the number you want to reverse: "))

def reverseDigits(num) -> int:

    sign = -1 if num<0 else 1 #store the sign before hand.
    num = abs(num) # made number postive

    rev = 0 # we are not using string to reverse. no type casting

    while num!=0:
        digit = num%10
        rev = rev*10 + digit
        num = num//10
    
    return sign*rev
    

print(reverseDigits(num))