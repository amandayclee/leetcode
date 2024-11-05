from collections import deque
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        if not moveTime or not moveTime[0]:
            return 0
        
        n, m = len(moveTime), len(moveTime[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        visited = [[float('inf')] * m for _ in range(n)]
        visited[0][0] = 0
        
        queue = deque([(0, 0, 0)])
        
        while queue:
            row, col, curr_time = queue.popleft()
            
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                
                if 0 <= new_row < n and 0 <= new_col < m:
                    next_time = max(curr_time + 1, moveTime[new_row][new_col] + 1)
                    
                    if next_time < visited[new_row][new_col]:
                        visited[new_row][new_col] = next_time
                        queue.append((new_row, new_col, next_time))
        
        return visited[n-1][m-1] if visited[n-1][m-1] != float('inf') else -1