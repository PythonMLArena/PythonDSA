from collections import deque

stack=deque()

stack.append(10) # adding the elements

stack.pop() # to remove the elements

# you can remove from the other end also 

not stack # to check whether the stack is empty or not 

from queue import LifoQueue

stack= LifoQueue(3) # maximum element we can add in 2

stack.put(10) # adding the elements

stack.get(timeout=1) # to remove the elements (need to set timeout to running) else it will keep searching unnecessary elements for long time




