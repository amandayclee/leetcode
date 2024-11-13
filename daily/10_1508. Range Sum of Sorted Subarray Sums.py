from heapq import heappop, heappush
from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 1000000007  # 1e9 + 7
        subarray_sum = []
        
        for i in range(len(nums)):
            temp = 0
            for j in range(i, len(nums)):
                temp += nums[j]
                subarray_sum.append(temp)
        
        subarray_sum.sort()
        
        return sum(subarray_sum[left - 1:right]) % MOD
    
# TC O(n^2 log n^2)
# SC O(n^2)
    
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 1000000007
        heap = []
        
        for i in range(n):
            heappush(heap, (nums[i], i, i))
            
        result = 0
        for k in range(right):
            curr_sum, start, end = heappop(heap)
            
            if k >= left - 1:
                result = (result + curr_sum) % MOD
        
            if end + 1 < n:
                next_sum = curr_sum + nums[end + 1]
                heappush(heap, (next_sum, start, end + 1))

        return result
    
# TC O(right * log n)
# SC O(n) max heap