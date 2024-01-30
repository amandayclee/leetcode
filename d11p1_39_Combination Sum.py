from typing import List
#
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.dfs(0, candidates, target, [], 0, res)
        
    def dfs(self, start, nums, target, path, current_sum, res):
        if current_sum == target:
            res.append(path.copy())
            return
        
        for i in range(start, len(nums)):
            if current_sum + nums[i] > target:
                continue
            
            path.append(nums[i])
            current_sum += nums[i]
            
            self.dfs(i, nums, target, path, current_sum, res)
            
            current_sum -= nums[i]
            path.pop()
            

if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": ([2,3,6,7], 7), "expected_output": [[2,2,3],[7]]},
        {"input": ([2,3,5], 8), "expected_output": [[2,2,2,2],[2,3,3],[3,5]]},
        {"input": ([2], 1), "expected_output": []}
    ]
    for test_case in test_cases:
        assert solution.combinationSum(test_case["input"][0], test_case["input"][1]) == test_case["expected_output"]
        

