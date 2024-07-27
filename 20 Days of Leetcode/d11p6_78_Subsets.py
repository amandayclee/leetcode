from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs(nums, [])
        return self.res
        
    def dfs(self, nums, path):
        self.res.append(path[:])
        
        for i in range(len(nums)):
            path.append(nums[i])
            self.dfs(nums[i + 1:], path)
            path.pop()

if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": ([1,2,3]), "expected_output": [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]}
    ]
    for test_case in test_cases:
        assert solution.subsets(test_case["input"]) == test_case["expected_output"]