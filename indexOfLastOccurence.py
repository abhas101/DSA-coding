# This program will find the last occurence of an element in a sorted array using binary search algo.

arr = [5,10,10,20,20]
target = 20
# expected output = 4

def indexOfLastOccurence(arr,target) -> int:
    low = 0
    high = len(arr)-1
    while(low<=high):
        # calculate mid in every iteraiton 
        mid = (low+high)//2
        
        if(arr[mid]<target):
            low = mid+1
        elif(arr[mid]>target):
            high = mid-1
        else:
            # if we reach to last, or right elemtn is not equals to the arr[mid] then return else move to right
            if(mid==high or arr[mid]!=arr[mid+1]):
                return mid
            else:
                low = mid+1
    
    return -1
# if the element is not present.

print(indexOfLastOccurence(arr,target))
    