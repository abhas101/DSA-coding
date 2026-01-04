# anagram optimised
s1 = "car"
s2 = "rac"

def checkanagram(s1:str,s2:str)->bool:
    s1.lower()
    s2.lower()
    arr = [0]*26 #we used this as a mapper, we are mapping char

    if(len(s1)!=len(s2)):
        return False

    for i in range(len(s1)):
        arr[ord(s1[i])-ord('a')] +=1 #we are checking the index, if 'b == 98, then b-a, 98-97 = 1, which is b's index in array. increment count

    for i in range(len(s2)):
        arr[ord(s2[i])-ord('a')] -=1 same, decrement count

  # if except zero, anything is there, then it is not anagram
    for item in arr:
        if(item!=0):
            return False
        
    return True


print(checkanagram(s1,s2))
