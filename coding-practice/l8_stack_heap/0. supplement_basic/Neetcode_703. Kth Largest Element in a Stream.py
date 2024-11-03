import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = nums
        self.k = k
        
        heapq.heapify(self.min_heap) # O(n)
        while len(self.min_heap) > k: # O(n-k)
            heapq.heappop(self.min_heap) # O(log n)
       
    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val) # TC O(log k)
        
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap) # TC O(log k)
        
        return self.min_heap[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)[:k]
        
    # TC O(n log n)
        
    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            self.nums.append(val)
        elif val > self.nums[-1]:
            self.nums[-1] = val
        self.nums.sort(reverse=True)
        return self.nums[-1]
    
    # TC O(k log k)