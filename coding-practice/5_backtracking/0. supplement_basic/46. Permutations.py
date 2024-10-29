from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs_helper([], nums)
        return self.res
        
    def dfs_helper(self, temp, remaining):
        if len(remaining) == 0:
            self.res.append(temp[:])
            return
        
        for i in range(len(remaining)):
            copy = remaining[:]
            temp.append(copy.pop(i))
            self.dfs_helper(temp, copy)
            temp.pop()
            
Solution().permute([1,2,3])

# O(n!)
# O(n^2) stack level = n, deep copy = n 