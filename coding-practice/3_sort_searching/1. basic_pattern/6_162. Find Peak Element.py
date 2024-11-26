from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left + 1 < right:
            mid = (left + right) // 2
            
            if nums[mid] < nums[mid + 1]: # 走上坡，往右找
                left = mid
            else:
                right = mid # 走下坡，peak 在左邊或者是當下的位置
                
        if nums[left] > nums[right]:
            return left
        return right
    
# TC O(log n) 每次變成數組長度的一半
# SC O(1)