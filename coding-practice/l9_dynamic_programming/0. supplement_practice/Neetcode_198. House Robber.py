from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.dfs(0, nums)
        
    def dfs(self, idx, nums):
        if idx >= len(nums):
            return 0
        return max(self.dfs(idx + 1, nums), nums[idx] + self.dfs(idx + 2, nums))
    
    
# TC O(2^n)
# SC O(n) stack call is as deep as n

class Solution:
    def rob(self, nums: List[int]) -> int:
        self.memo = {}
        return self.dfs(0, nums)
    
    def dfs(self, idx, nums):
        if idx >= len(nums):
            return 0
        
        if idx in self.memo:
            return self.memo[idx]
        
        self.memo[idx] = max(self.dfs(idx + 1, nums), nums[idx] + self.dfs(idx + 2, nums))
        
        return self.memo[idx]
    
# TC O(n)
# SC O(n)

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums) if nums else 0
        
        dp = [0] * len(nums)  # 改成 len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        
        return dp[-1] 
    
# TC O(n)
# SC O(n)

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return max(nums) if nums else 0
        
        dp = [nums[0], max(nums[0], nums[1])]
        
        for i in range(2, len(nums)):
            temp = dp[1]
            dp[1] = max(nums[i] + dp[0], dp[1])
            dp[0] = temp
        
        return dp[1]
    
# TC O(n)
# SC O(1)