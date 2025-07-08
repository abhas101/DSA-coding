# Print N to 1 using recursion and print 1 to N using Recursion

n = 10

def funNto1(n):
    
    # base case, if n becomes, zero, we stop
    if(n==0):return
    
    # printng 10,
    print(n)
    
    funNto1(n-1)#then calling for 9. In the same way it will proceed. This is tail recusive

funNto1(n)

# Function to print 1 to N using Recursion
def fun1toN(n:int)->None:
    if(n==0):return
    fun1toN(n-1)#Here it will go to 1, store it and then start printing.
    print(n)    #this is not tail recursive
    
fun1toN(n)
    
