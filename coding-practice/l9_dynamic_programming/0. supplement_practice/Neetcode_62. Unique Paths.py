class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.cache = [[0] * n for _ in range(m)]
        return self.dfs(0, 0, m, n)
        
        
    def dfs(self, row, col, rows, cols):
        if row == rows or col == cols:
            return 0
        
        if row == rows - 1 and col == cols - 1:
            return 1
        
        if self.cache[row][col] != 0:
            return self.cache[row][col]
        
        self.cache[row][col] = self.dfs(row + 1, col, rows, cols) + self.dfs(row, col + 1, rows, cols)
        
        return self.cache[row][col]
        
# TC O(m * n)
# SC O(m * n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows, cols = m, n
        prev_row = [0] * cols
        
        for row in range(rows - 1, -1, -1):
            cur_row = [0] * cols
            cur_row[-1] = 1
            for col in range(cols - 2, -1, -1):
                cur_row[col] = prev_row[col] + cur_row[col + 1]
            prev_row = cur_row
        
        return prev_row[0]
# TC O(m * n)
# SC O(n)