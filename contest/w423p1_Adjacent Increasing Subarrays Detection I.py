from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if len(nums) < 2 * k:
            return False
            
        if k == 1:
            return True
            
        for i in range(len(nums) - 2 * k + 1):
            if self.check_k_increase(nums, i, k) and self.check_k_increase(nums, i + k, k):
                return True
        return False
        
    def check_k_increase(self, nums, start_idx, k):
        for i in range(start_idx, start_idx + k - 1):
            if nums[i] >= nums[i + 1]:
                return False
        return True
    
# TC O(n^2)
# SC O(1)