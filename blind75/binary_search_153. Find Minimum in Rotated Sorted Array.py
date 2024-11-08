from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        
        return self.binary_search(nums, 0, len(nums) - 1)
    
    
    def binary_search(self, nums, left, right) -> int:
        if left + 1 == right:
            return min(nums[left], nums[right])
        
        mid = (left + right) // 2
        
        # base case
        if mid > 0 and nums[mid] < nums[mid-1]:
            return nums[mid]

        if nums[mid] > nums[right]:
            return self.binary_search(nums, mid, right)
        else: # nums[mid] <= nums[right]
            return self.binary_search(nums, left, mid)
        
Solution().findMin([3,4,5,1,2])