from collections import deque

q=deque()

# add the element to the queue
q.appendleft(10) # adding from back 
q.append(10) # adding element from other end

q.pop() # remove from front 
q.popleft(0) # remove from other end


import queue
from queue import Queue

q=Queue()
q.put(10)  # to add element in  queue
q.get() # to remove element from queue


