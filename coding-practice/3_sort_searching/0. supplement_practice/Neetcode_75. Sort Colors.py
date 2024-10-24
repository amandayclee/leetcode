from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        
        for num in nums:
            counts[num] += 1
            
        idx = 0
        for color in counts:
            for freq in range(counts[color]):
                nums[idx] = color
                idx += 1
        