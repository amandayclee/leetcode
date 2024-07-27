from collections import deque

class Solution:
   def __init__(self):
       self.grid = []
       self.n = 0
       self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
  
   def dfs(self, x, y):
       if x < 0 or x >= self.n or y < 0 or y >= self.n or self.grid[x][y] != 1:
           return
       self.grid[x][y] = 2  # Marking the cell as part of the first island
       for dx, dy in self.directions:
           self.dfs(x + dx, y + dy)

   def bfs(self):
       queue = deque()
       for i in range(self.n):
           for j in range(self.n):
               if self.grid[i][j] == 2:  # Cells belonging to the first island
                   queue.append((i, j, 0))  # (x, y, distance)

       while queue:
           x, y, dist = queue.popleft()
           for dx, dy in self.directions:
               nx, ny = x + dx, y + dy
               if 0 <= nx < self.n and 0 <= ny < self.n:
                   if self.grid[nx][ny] == 1:  # Part of the second island
                       return dist
                   elif self.grid[nx][ny] == 0:  # Water, can be flipped
                       self.grid[nx][ny] = -1  # Mark as visited
                       queue.append((nx, ny, dist + 1))
       return -1  # In case islands are already connected or input is invalid

   def shortestBridge(self, grid):
       self.grid = grid
       self.n = len(grid)
      
       # Find and mark the first island
       found = False
       for i in range(self.n):
           for j in range(self.n):
               if self.grid[i][j] == 1:
                   self.dfs(i, j)
                   found = True
                   break
           if found:
               break

       # Use BFS to expand from the first island and find the shortest path to the second
       return self.bfs()
   

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        {"input": ([
  [0, 1, 1, 0],
  [0, 1, 0, 0],
  [0, 0, 0, 0],
  [0, 0, 1, 1]
]), "expected_output": 2}
    ]
    for test_case in test_cases:
        assert solution.shortestBridge(test_case["input"]) == test_case["expected_output"]