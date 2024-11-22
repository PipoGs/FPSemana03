from collections import deque

inputnum = input()

inputnumsplit = inputnum.split(" ")

stack = deque()

for k in inputnumsplit:
    
    n1 = int(k)
    
    stack.append(n1)

print(stack)

for i in range(len(stack)):
    
    stck = stack.pop()
    
    print(int(stck)**2)
