# this program is using binary search to find the first index of a target in a sorted array.

arr = [5,10,10,20,20]
target = 10
# expected output = 1

def indexOfFirstOccurance(arr,target):
    low = 0
    high = len(arr)-1
    
    while(low<=high):
        mid = (low+high)//2
        
        if(arr[mid]<target):
            low = mid+1
        elif(arr[mid]>target):
            high = mid-1
        else:
            # we are checking if mid is the last index, or arr[mid] is not equal to the previous element which
            # means that we are at the first occurance. otherwise we move left
            if(mid==0 or arr[mid]!=arr[mid-1]):
                return mid
            else:
                high = mid-1
    
    return -1
# if the element is not present.

print(indexOfFirstOccurance(arr,target))