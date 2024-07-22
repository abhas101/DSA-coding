# searcing in a linked list

# created a class Node and it's constructior
class Node:
    def __init__(self,k) -> None:
        self.key = k
        self.next = None 

    
# function to search in a linked list   
def searchList(head,target) -> int:
    curr = head
    count = 1
    while(curr!=None):
        if(curr.key==target): return count
        else:
            count+=1
            curr=curr.next
    return -1


# creating Nodes of linked list or objects 
head = Node(10)
head.next= Node(5)
head.next.next= Node(30)
head.next.next.next= Node(15)


# test 

target = 30
#expected  output = 3
print(searchList(head,target))