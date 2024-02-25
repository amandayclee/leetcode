import heapq

def heap_example():
    l = []
    heapq.heapify(l)
    
    # l is a heap now
    # in python, heap is a min heap
    
    min_element = heapq.heappop(l)
    
    item = 1
    heapq.heappush(l, item)
    
    
    # if we want to use a max heap
    
    inverted_list = []
    for element in l:
        inverted_list.append(-element)
    
    max_heap = heapq.heapify(inverted_list)
    
    max_element = -heapq.heappop(l)
    
    heapq.heappush(l, -item)

    # median of two streams
    # if abs(len(max_heap) - len(min_heap)) > 2:
        # do balance
    


