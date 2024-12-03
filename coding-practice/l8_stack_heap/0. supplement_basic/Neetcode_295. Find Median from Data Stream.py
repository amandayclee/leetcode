import heapq


class MedianFinder:

    def __init__(self):
        self.small_max_heap = []
        self.big_min_heap = []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_max_heap, -1 * num)
        
        if (self.small_max_heap and self.big_min_heap) and \
            (self.small_max_heap[0] * -1 > self.big_min_heap[0]):
                heapq.heappush(self.big_min_heap, -1 * heapq.heappop(self.small_max_heap))
        
        if len(self.small_max_heap) > len(self.big_min_heap) + 1:
                heapq.heappush(self.big_min_heap, -1 * heapq.heappop(self.small_max_heap))
        
        if len(self.small_max_heap) + 1 < len(self.big_min_heap):
            heapq.heappush(self.small_max_heap, -1 * heapq.heappop(self.big_min_heap))        

# m is the number of function calls
# TC O(log n)

    def findMedian(self) -> float:
        if len(self.small_max_heap) > len(self.big_min_heap):
            return self.small_max_heap[0] * -1
        elif len(self.small_max_heap) < len(self.big_min_heap):
            return self.big_min_heap[0]
        else:
            return (self.small_max_heap[0] * -1 + self.big_min_heap[0]) / 2.0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()