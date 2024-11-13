from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        return self.dfs(0, 0, obstacleGrid)
        
    def dfs(self, row, col, obstacleGrid):
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        
        if row == rows or col == cols or obstacleGrid[row][col] == 1:
            return 0
        
        if row == rows - 1 and col == cols - 1:
            return 1

        return self.dfs(row + 1, col, obstacleGrid) + self.dfs(row, col + 1, obstacleGrid)
        
# TLE

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.cache = [[0] * len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        return self.dfs(0, 0, obstacleGrid)
        
    def dfs(self, row, col, obstacleGrid):
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        
        if row == rows or col == cols or obstacleGrid[row][col] == 1:
            return 0
        
        if row == rows - 1 and col == cols - 1:
            return 1

        if self.cache[row][col] != 0:
            return self.cache[row][col]
        
        self.cache[row][col] =  self.dfs(row + 1, col, obstacleGrid) + self.dfs(row, col + 1, obstacleGrid)
        
        return self.cache[row][col]

# TC O(m * n)
# SC O(m * n)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
            
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        prev_row = [0] * n
        
        # 初始化最後一行
        prev_row[n-1] = 1 if obstacleGrid[m-1][n-1] == 0 else 0
        for col in range(n-2, -1, -1):
            if obstacleGrid[m-1][col] == 0:
                prev_row[col] = prev_row[col+1]
        
        # 從倒數第二行開始向上處理
        for row in range(m-2, -1, -1):
            cur_row = [0] * n
            # 處理最右列
            cur_row[n-1] = prev_row[n-1] if obstacleGrid[row][n-1] == 0 else 0
            
            for col in range(n-2, -1, -1):
                if obstacleGrid[row][col] == 0:
                    cur_row[col] = cur_row[col+1] + prev_row[col]
            
            prev_row = cur_row
        
        return prev_row[0]
    
# TC O(m * n)
# SC O(n)