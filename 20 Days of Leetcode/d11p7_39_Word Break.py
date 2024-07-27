import collections
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = collections.defaultdict(bool)  # default false
        return self.dfs(s, wordDict, len(s), memo)
    
    def dfs(self, s, wordDict, start_idx, memo):
        if start_idx == len(s):
            memo[start_idx] = True  # base case if we can get the last idx
            return True
            
        for i in range(len(s), start_idx, -1):
            substring = s[len(s):start_idx + i]
            if substring in wordDict:
                if self.dfs(s, wordDict, start_idx + i, memo):
                    memo[start_idx] = True
                    return True
                
                
        memo[start_idx] = False
        return False

if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": (["applepenapple", ["apple","pen"]]), "expected_output": True}
    ]
    for test_case in test_cases:
        assert solution.wordBreak(test_case["input"][0], test_case["input"][1]) == test_case["expected_output"]