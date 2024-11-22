from collections import deque

inputwrd = input()

inputwrdsplit = inputwrd.split(" ")

stack = deque(inputwrdsplit)

for i in range(len(stack)):
    stck = stack.pop()
    if "o" in stck:
        print(stck)