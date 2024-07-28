# binary tree

# Defining binary tree
class Node:
    def __init__(self,k) -> None:
        self.right = None
        self.left = None
        self.key = k 
        
# creating binary tree 

root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.right.left = Node(40)
root.right.right = Node(50)

# printing binary tree

# inorder traversal
def inorder(root):
    if(root!=None):
        inorder(root.left)
        print(root.key,end=" ")
        inorder(root.right)

# preorder traversal
def preOrder(root):
    if(root!=None):
        print(root.key,end = " ")
        preOrder(root.left)
        preOrder(root.right)

# post order traversal  
def postOrder(root):
    if(root!=None):
        postOrder(root.left)
        postOrder(root.right)
        print(root.key,end=" ")
