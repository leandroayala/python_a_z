#queues is while first-in first-out

#To implement a queue, we will use package collection.deque wich was designed to have fast appends and pops both ends.
#to use package collection lets import for our file this way
from collections import deque

#here we are using package collection: function deque 
queue = deque(['John','Mari','Jesus'])
queue.append('petter') #petter added to queue

queue.popleft()  # The first to arrive now leaves . john leaves
print(queue)

#to execute this on the terminal type: py .\4_data_structures\3_list_as_queues.py