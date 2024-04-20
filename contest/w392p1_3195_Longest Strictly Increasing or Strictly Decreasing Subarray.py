from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        count = 1
        max_count = 1
        direction = None
        
        for i in range(1, len(nums)):
            if (nums[i - 1] < nums[i]):
                if direction == -1 or direction is None:
                    direction = 1
                    count = 2
                else:
                    count += 1
            elif (nums[i - 1] > nums[i]):
                if direction == 1 or direction is None:
                    direction = -1
                    count = 2
                else:
                    count += 1
            else:
                count = 1
            
            max_count = max(count, max_count)
        
        return max_count
                
         