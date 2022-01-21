
# can use Python's PriorityQueue module
# insert with put and get priority element with get

import queue

q = queue.PriorityQueue()
q.put(1)
q.put(6)
q.put(2)
q.put(4)
q.put(7)
print(q.get()) # 1
print(q.get()) # 2
print(q.get()) # 4



# heapq module
# heaps are binary trees 
# minheap -> every parent node has a value <= to its children
# maxheap -> every parent node has a value >= to its children
# heaps are not always sorted

# time complexity of heappush and heappop is O(log n)
# heapify is O(n)

import heapq

heap = []
heapq.heappush(heap, 10)
print(heap) # [10]
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)
print(heap) # [1, 10, 5]

#   1
#  / \
# 10  5

print(heap[0]) # prints 1; 0 index has minimum value
heapq.heappop(heap) # deletes 1
print(heap) # [5, 10]
heapq.heappop(heap)
print(heap) # [10]

# heapify converts list to a heap
list1 = [7,3,5,2,1,6]
heapq.heapify(list1)
print(list1) # [1, 2, 5, 7, 3, 6]
print(heapq.heappop(list1)) # 1
print(heapq.heappop(list1)) # 2
print(len(list1)) # 4


# nsmallest, nlargest
print(heapq.nsmallest(2, list1)) # [1,2]
print(heapq.nlargest(3,list1))