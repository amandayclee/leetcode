from collections import defaultdict
from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        count = [0] * (len(nums) + 1)
        
        for left, right in queries:
            count[left] += 1
            count[right + 1] -= 1
        
        prefix = 0
        for i in range(len(nums)):
            prefix += count[i]
            count[i] = prefix
            
        for i in range(len(nums)):
            if nums[i] - count[i] > 0:
                return False
        return True
    
print(Solution().isZeroArray([1,0,1], [[0,2]]))