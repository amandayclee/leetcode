from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        
        left = 0
        
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        
        return left
                

Solution().removeElement([0,1,2,2,3,0,4,2], 2)