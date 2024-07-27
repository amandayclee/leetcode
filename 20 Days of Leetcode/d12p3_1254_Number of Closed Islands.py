from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 and self.dfs(i, j, grid):
                    count += 1
        return count
    
    def dfs(self, x, y, grid):
        if grid[x][y] == 1:
            return True
        if not (0 < x < len(grid) - 1) or not (0 < y < len(grid[0]) - 1):
            return False
        
        grid[x][y] = 1
        up = self.dfs(x + 1, y, grid)
        down = self.dfs(x - 1, y, grid)
        right = self.dfs(x, y + 1, grid)
        left = self.dfs(x, y - 1, grid)
        
        return up and down and right and left

    
    def is_valid(self, x, y, grid):
        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
            return True
        return False
    
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        {"input": ([[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]), "expected_output": 1},
        {"input": ([[0,0,1,1,0,1,0,0,1,0],[1,1,0,1,1,0,1,1,1,0],[1,0,1,1,1,0,0,1,1,0],[0,1,1,0,0,0,0,1,0,1],[0,0,0,0,0,0,1,1,1,0],[0,1,0,1,0,1,0,1,1,1],[1,0,1,0,1,1,0,0,0,1],[1,1,1,1,1,1,0,0,0,0],[1,1,1,0,0,1,0,1,0,1],[1,1,1,0,1,1,0,1,1,0]]), "expected_output": 8}
    ]
    for test_case in test_cases:
        assert solution.closedIsland(test_case["input"]) == test_case["expected_output"]