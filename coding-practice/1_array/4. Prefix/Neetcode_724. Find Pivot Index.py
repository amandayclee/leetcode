from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Build prefix sum array
        prefix_table = [0] * (len(nums) + 1)
        for i in range(1, len(nums) + 1):
            prefix_table[i] = prefix_table[i-1] + nums[i-1]
        
        # Check each potential pivot
        for i in range(len(nums)):
            left_sum = prefix_table[i] - prefix_table[0]
            right_sum = prefix_table[-1] - prefix_table[i+1]
            
            if left_sum == right_sum:
                return i
                
        return -1
    
# TC O(n)
# SC O(n)