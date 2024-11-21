from typing import List


class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                if sum(nums[:i]) == sum(nums[i+1:]):
                    res += 2
                elif sum(nums[:i]) + 1 == sum(nums[i+1:]) or sum(nums[:i]) == sum(nums[i+1:]) + 1:
                    res += 1 
        
        return res
    
Solution().countValidSelections([16,13,10,0,0,0,10,6,7,8,7])