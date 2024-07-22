# Bubble sort is a simple comparision based algo which takes O(n2) time
# in the first pass, we move the largest element to the last and keep doing in the following passes.

arr = [0,10,2,0,304,45,0,1,1,1,1,7]

def bubbleSort(arr) -> list:
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if(arr[j]>arr[j+1]):   
                arr[j],arr[j+1]=arr[j+1],arr[j]
    
    return arr

bubbleSort(arr)

print(arr)