from collections import deque

inputnum = input()

inputnumsplit = inputnum.split(" ")

stack = deque(inputnumsplit)

print(stack)

for i in range(len(stack)):
    stck = stack.pop()
    print(int(stck)**2)