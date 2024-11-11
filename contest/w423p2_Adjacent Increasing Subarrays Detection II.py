from typing import List


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        
        left = [1] * n
        for i in range(1, n):
            if nums[i-1] < nums[i]:
                left[i] = left[i-1] + 1
                
        right = [1] * n
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                right[i] = right[i+1] + 1
        
        ans = 1

        for i in range(n-1):
            possible_k = min(left[i], right[i+1])
            if i + 1 + possible_k <= n:
                ans = max(ans, possible_k)
                
        return ans