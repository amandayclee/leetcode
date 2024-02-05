from typing import List
import collections


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    continue
                
                if visited[i][j]:
                    continue
                
                self.bfs(i, j, grid, visited)
                count += 1
        
        return count

        
    def bfs(self, x, y, grid, visited):
        visited[x][y] = True
        q = collections.deque([(x, y)])
        deltas = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        while q:
            x, y = q.popleft()
            
            for dx, dy in deltas:
                new_x = x + dx
                new_y = y + dy
                
                if not self.is_valid(grid, new_x, new_y):
                    continue
                
                if visited[new_x][new_y]:
                    continue
                
                if grid[new_x][new_y] == '0':
                    continue
                
                q.append((new_x, new_y))
                visited[new_x][new_y] = True
   
    
        
    def is_valid(self, grid, x, y):
        if -1 < x < len(grid) and -1 < y < len(grid[0]):
            return True
        return False
    
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        {"input": ([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]), "expected_output": 3}
    ]
    for test_case in test_cases:
        assert solution.numIslands(test_case["input"]) == test_case["expected_output"]