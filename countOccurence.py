
# Binary search
#This program will find the occurance of an element in a sorted array.
# we are using 3 functions, one for findings the first index, one for the last index and one to count the occurence.
# we will subtract the last index and first index, and add +1 in result. as indexing is 0 based.

# Function to find the first index using binary search
def firstIndex(arr,target) -> int:
    low = 0
    high = len(arr)-1
    while(low<=high):
        mid = (low+high)//2
        if(arr[mid]<target):
            low = mid+1
        elif(arr[mid]>target):
            high = mid-1
        else:
            if(mid==0 or arr[mid]!=arr[mid-1]):
                return mid
            else:
                high = mid-1
                 
    return -1

# funciton to find last index using binary search
def lastIndex(arr,target) -> int:
    
    low = 0
    high = len(arr)-1
    while(low<=high):
        mid = (low+high)//2
        if(arr[mid]<target):
            low = mid+1
        elif(arr[mid]>target):
            high = mid-1
        else:
            if(mid==high or arr[mid]!=arr[mid+1]):
                return mid
            else:
                low = mid+1     
    return -1


#  function to find the count the occurence.

def Count(arr,target) -> int:
    first = firstIndex(arr,target)
    last =  lastIndex(arr,target)
    
    if(first == -1):
        return 0
    else:
        return last-first+1


# test

arr = [10,20,20,20,30,30]
target = 20
# expected output = 3

print(Count(arr,target))