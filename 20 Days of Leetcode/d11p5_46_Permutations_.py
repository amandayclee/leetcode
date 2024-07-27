from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs(nums, [])
        return self.res
    
    def dfs(self, nums, temp):
        # base case
        if len(nums) == 0:
            self.res.append(temp[:])
            return
        
        for i in range(len(nums)):
            temp.append(nums[i])
            # print('nums[:i]', nums[:i])
            # print('nums[i + 1:]', nums[i + 1:])
            # print('nums[:i] + nums[i + 1:]', nums[:i] + nums[i + 1:])
            self.dfs(nums[:i] + nums[i + 1:], temp)
            temp.pop()
            
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": ([1,2,3]), "expected_output": [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]}
    ]
    for test_case in test_cases:
        assert solution.permute(test_case["input"]) == test_case["expected_output"]