from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)
        
        # reverse whole array
        left, right = 0, len(nums) - 1
        self.reverse_helper(left, right, nums)
        
        # reverse first k
        left, right = 0, k - 1
        self.reverse_helper(left, right, nums)
        
        # reverse remaining
        left, right = k, len(nums) - 1
        self.reverse_helper(left, right, nums)
        
    def reverse_helper(self, left, right, nums):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
            
# TC O(n)
# SC O(1)

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)
        temp = [0] * len(nums)
        
        for i in range(len(nums)):
            new_idx = (i + k) % len(nums)
            temp[new_idx] = nums[i]
        
        for i in range(len(nums)):
            nums[i] = temp[i]
            
# TC O(n)
# SC O(n)