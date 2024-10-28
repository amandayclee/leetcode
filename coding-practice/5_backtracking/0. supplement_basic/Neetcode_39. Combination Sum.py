from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.target = target
        self.candidates = candidates
        self.res = []
        self.dfs_helper(0, [], 0)
        
        return self.res
    
    def dfs_helper(self, index, temp, curr_sum):
        if curr_sum == self.target:
            self.res.append(temp[:])
            return
        
        if curr_sum > self.target:
            return
        
        for i in range(index, len(self.candidates)):
            temp.append(self.candidates[i])
            self.dfs_helper(i, temp, curr_sum + self.candidates[i])
            temp.pop()

        

print(Solution().combinationSum([2, 3, 6, 7], 7))

# O(N^(T/M))
# N = candidates 的長度
# T = target 值
# M = candidates 中最小的數字
# O(T/M)
# 遞迴深度