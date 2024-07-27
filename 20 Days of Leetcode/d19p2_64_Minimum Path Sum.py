from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        
        res = [[float("inf")] * (COLS + 1) for r in range(ROWS + 1)]
        print(res)
        res[ROWS - 1][COLS] = 0
        
        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                res[r][c] = grid[r][c] + min(res[r + 1][c], res[r][c + 1])
        
        return res[0][0]
    

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        {"input": ([[1,3,1],[1,5,1],[4,2,1]]), "expected_output": 7},
        {"input": ([[1,2,3],[4,5,6]]), "expected_output": 12},
        
    ]
    for test_case in test_cases:
        assert solution.minPathSum(test_case["input"]) == test_case["expected_output"]
