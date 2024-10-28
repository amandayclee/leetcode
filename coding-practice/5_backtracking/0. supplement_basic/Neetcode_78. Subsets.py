from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs_helper(nums, 0, [])
        
        return self.res
        
    def dfs_helper(self, nums, index, temp):
        if index >= len(nums):
            self.res.append(temp[:])
            return
        
        temp.append(nums[index])
        self.dfs_helper(nums, index + 1, temp)
        
        temp.pop()
        self.dfs_helper(nums, index + 1, temp)