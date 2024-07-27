from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res = []
        self.dfs(1, n, k, [])
        return self.res

    def dfs(self, start, n, k, temp):
        if k == 0:
            self.res.append(temp[:])  # deep copy temp
            return
        
        for i in range(start, n + 1):
            temp.append(i)
            self.dfs(i + 1, n, k - 1, temp)
            temp.pop()
        return

if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": (4, 2), "expected_output": [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]}
    ]
    for test_case in test_cases:
        assert solution.combine(test_case["input"][0], test_case["input"][1]) == test_case["expected_output"]