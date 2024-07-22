# This program is creating a linkedlist and printing it.

# creating a  class Node
class Node:
    def __init__(self,k) -> None:
        self.key = k
        self.next = None

# Printing the list 
def printList(head):
    curr = head
    while(curr!=None):
        print(curr.key,end =" ")
        curr = curr.next 

# creating nodes
head= Node(10)
head.next = Node(20)
head.next.next = Node(30)


printList(head) 