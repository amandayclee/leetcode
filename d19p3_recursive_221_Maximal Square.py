from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # dynamic programming: bottom up
        # recursive: top down <--- this solution
        
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = {} # match each (r, c) -> maxArea
        
        # T: O(m*n) M: O(m*n)
        def helper(r, c):
            if r >= ROWS or c >= COLS:
                return 0
            
            if (r, c) not in cache:
                down = helper(r + 1, c)
                right = helper(r, c + 1)
                diagnol = helper(r + 1, c + 1)
            
                cache[(r, c)] = 0
                if matrix[r][c] == "1":
                    cache[(r, c)] = 1 + min(down, right, diagnol)
            
            return cache[(r, c)]
        
        helper(0, 0)
        
        return max(cache.values()) ** 2
    
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        {"input": ([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]), "expected_output": 4},
        {"input": ([["0","1"],["1","0"]]), "expected_output": 1},
    ]
    for test_case in test_cases:
        assert solution.maximalSquare(test_case["input"]) == test_case["expected_output"]
