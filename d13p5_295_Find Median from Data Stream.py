import heapq

class MedianFinder:

    def __init__(self):
        self.min_heap_for_large_num = []
        self.max_heap_for_small_num = []

    def addNum(self, num: int) -> None:
        min_heap_len = len(self.min_heap_for_large_num)
        max_heap_len = len(self.max_heap_for_small_num)
        
        # python only has min heap in heapq package
        # so we need to negate the numbers in max heap
        if self.max_heap_for_small_num and num < -1 * self.max_heap_for_small_num[0]:
            heapq.heappush(self.max_heap_for_small_num, -1 * num)
        elif self.min_heap_for_large_num and num > self.min_heap_for_large_num[0]:
            heapq.heappush(self.min_heap_for_large_num, num)
        else:
            if max_heap_len < min_heap_len:
                heapq.heappush(self.max_heap_for_small_num, -1 * num)
            else:
                heapq.heappush(self.min_heap_for_large_num, num)
        self.rebalance()
    
    def rebalance(self):
        min_heap_len = len(self.min_heap_for_large_num)
        max_heap_len = len(self.max_heap_for_small_num)
        
        if max_heap_len > min_heap_len:
            if max_heap_len - min_heap_len > 1:
                num_to_move = -1 * heapq.heappop(self.max_heap_for_small_num)
                heapq.heappush(self.min_heap_for_large_num, num_to_move)
        else:
            if min_heap_len - max_heap_len > 1:
                num_to_move = heapq.heappop(self.min_heap_for_large_num)
                heapq.heappush(self.max_heap_for_small_num, -1 * num_to_move)

    def findMedian(self) -> float:
        min_heap_len = len(self.min_heap_for_large_num)
        max_heap_len = len(self.max_heap_for_small_num)
        
        if min_heap_len == max_heap_len:
            median = (self.min_heap_for_large_num[0] - self.max_heap_for_small_num[0]) / 2
        else:
            if max_heap_len > min_heap_len:
                median = -1 * self.max_heap_for_small_num[0]
            else:
                median = self.min_heap_for_large_num[0]

        return median
    
    
# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()