# Question - Given an array of positive repeating Integers, you need to find the  only one number which is repeating odd number of time

arr1 = [10,30,30,10,30,30,20]
arr2 = [10,10,10,10,10,20,20]
arr3 = [10,10,20,30,30,20,40]
arr4 = [10]

# ---------------------------- Total 3 methods covered
# Naive 2 traversal Approach
# For each element, we are going to count how many times it is repeated in an array.
# Then we check if count is odd, return count.

def findOdd(arr):
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr)):
            if arr[i] == arr[j]:
                count += 1
        
        if(count%2!=0): return arr[i]


print(findOdd(arr1))
print(findOdd(arr2))
print(findOdd(arr3))
print(findOdd(arr4))
print()
# ---------------------------

# ---------------------------

# Better approach using the count built-in function. We are counting elements, and as soon as we find one odd repeating, we will return the item.
def findOdd2(arr):
    
    for item in arr:
        if (arr.count(item) %2!=0):
            return item
print(findOdd2(arr1))
print(findOdd2(arr2))
print(findOdd2(arr3))
print(findOdd2(arr4))
print()

# --------------------------

# -------------------------
    # we are going to use XOR operator. 
    #Properties of XOR is x ^ x = 0 and x ^ 0 = x
def findOddBitwise(arr):

    res = 0
    for item in arr:
        res = res ^ item
    
    return res



print(findOddBitwise(arr1))
print(findOddBitwise(arr2))
print(findOddBitwise(arr3))
print(findOddBitwise(arr4))

# End code.
