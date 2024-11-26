from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 1 
        while right < len(nums):
            if nums[left] != nums[right]:
                nums[left + 1] = nums[right]
                left += 1
            right += 1
            
        return left + 1
                
# TC O(n)
# SC O(1)