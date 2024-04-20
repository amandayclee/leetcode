from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        gains = [0] * (len(prices) - 1)
        
        for i in range(1, len(prices)):
            gains[i - 1] = prices[i] - prices[i - 1]
        
        return max(0, self.max_subarray(gains))


    def max_subarray(self, nums):
        arr = [0] * len(nums)
        arr[0] = nums[0]
        
        for i in range(1, len(nums)):
            arr[i] = max(arr[i - 1] + nums[i], nums[i])
                
        return max(arr)