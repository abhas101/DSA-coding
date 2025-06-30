# Given an array of integers, arr[]. Find if there is a subarray (of size at least one) with 0 sum. Return true/false depending upon whether there is a subarray present with 0-sum or not. 
# input
arr1 = [1,4,13,-3,-10,5]
arr2 = [-1,4,-3,5,1]
arr3 = [3,1,-2,5,6]
arr4 = [5,6,0,8]


# we are going to use efficient sol'n which finds the subarray in one traversal
def zeroSum(arr):
  
    n = len(arr)
  # we will use set and preFix sum method to find
  # if the prefixSum is repeating in an array, then it has subarray for zero sum.
    h = set()
    sum = 0
  
    for i in range(n):
        sum+=arr[i]
      # sum==0 will be used for cases , where prfix sum itself is zero and not repeating. [3,-2,-1] Here, prefix sum is [3,1,0]; however, we have sa ubarray with zero sum.
        if(sum ==0 or sum in h): return True
        else:
            h.add(sum) #add the prefix to the set to keep track of repeating
            
    return False

print(zeroSum(arr1))
print(zeroSum(arr2))
print(zeroSum(arr3))
print(zeroSum(arr4))
