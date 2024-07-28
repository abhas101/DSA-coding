s = "{(([]))}"

def balanced(s) -> bool:
    stack = []
    
    for i in range(len(s)):
        if(s[i]=='(' or s[i]=='[' or s[i]=='{'):
            stack.append(s[i])
        else:
            # if someone put closing at first, then the stack will be empty, and underflow error.
            if not stack: return False 
            elif( isMatching(stack[-1],s[i])==False): return False
            else:
                stack.pop()
                
    # if some chararcter left in stack, then it is not balanced. 
    if(stack):
        return False
    else:
        return True
  
  

def isMatching(open,closed) -> bool:
    if(open=='(' and closed == ')') or (open=='[' and closed ==']') or (open =='{' and closed =="}"):
        return True
    else:
        return False
    
         
print(balanced(s)) 