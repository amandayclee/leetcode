from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        longest_lenght = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == "1":
                    dp[r + 1][c + 1] = 1 + min(dp[r][c], dp[r + 1][c], dp[r][c + 1])
                    longest_lenght = max(longest_lenght, dp[r + 1][c + 1])
                    
        return longest_lenght ** 2
        

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        {"input": ([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]), "expected_output": 4},
        {"input": ([["0","1"],["1","0"]]), "expected_output": 1},
    ]
    for test_case in test_cases:
        assert solution.maximalSquare(test_case["input"]) == test_case["expected_output"]
