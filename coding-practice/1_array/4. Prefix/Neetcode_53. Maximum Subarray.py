from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return max(self.dfs(i, nums) for i in range(len(nums)))

    def dfs(self, idx, nums):
        if idx == len(nums):
            return float('-inf')
        
        return max(
            nums[idx],  
            nums[idx] + self.dfs(idx + 1, nums)
        )

# TC O(N^2)
# SC O(N)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        self.memo = {}
        return max(self.dfs(i, nums) for i in range(len(nums)))

    def dfs(self, idx, nums):
        if idx == len(nums):
            return float('-inf')
            
        if idx in self.memo:
            return self.memo[idx]
            
        self.memo[idx] = max(
            nums[idx],
            nums[idx] + self.dfs(idx + 1, nums)
        )
        return self.memo[idx]

# TC O(N)
# SC O(N)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        # dp[i] = 以 i 結尾的最大子數組和
        dp = [0] * n
        dp[0] = nums[0]
        
        for i in range(1, n):
            dp[i] = max(
                nums[i],
                nums[i] + dp[i - 1]                
            )
            
        return max(dp)
    
# TC O(N)
# SC O(N)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = cur_sum = nums[0]
        
        for num in nums[1:]:
            cur_sum = max(num, cur_sum + num)
            max_sum = max(max_sum, cur_sum)
    
        return max_sum
    
# TC O(N)
# SC O(1)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        cur_sum = 0
        
        for num in nums:
            cur_sum = max(cur_sum, 0) + num
            max_sum = max(max_sum, cur_sum)
    
        return max_sum
    
# TC O(N)
# SC O(1)