from collections import deque

inputwrd = input()

inputwrdsplit =(inputwrd.split(" "))

stack = deque()

for k in inputwrdsplit:
    
    stack.appendleft(k)

print (stack)

for i in range(len(stack)):
    
    stck = stack.pop()
    
    
    if "o" in stck:
        print(stck)