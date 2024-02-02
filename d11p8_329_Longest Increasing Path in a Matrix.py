from typing import List
import collections


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row, col = len(matrix), len(matrix[0])
        lip_board = [[0 for _ in range(col)] for _ in range(row)]
        deltas = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        
        for x in range(row):
            for y in range(col):
                for dx, dy in deltas:
                    new_x = x + dx
                    new_y = y + dy
                    if not self.in_bound(new_x, new_y, matrix):
                        continue
                    
                    if matrix[new_x][new_y] < matrix[x][y]:
                        lip_board[x][y] += 1
        
        q = collections.deque([])
        for x in range(row):
            for y in range(col):
                if lip_board[x][y] == 0:
                    q.append((x, y))
        
        res = 0
        while q:
            for _ in range(len(q)):
                x, y = q.popleft()
                for dx, dy in deltas:
                    nw_x = x + dx
                    nw_y = y + dy
                    
                    if not self.in_bound(nw_x, nw_y, matrix):
                        continue
                    
                    if matrix[nw_x][nw_y] > matrix[x][y]:
                        lip_board[nw_x][nw_y] -= 1
                        if lip_board[nw_x][nw_y] == 0:
                            q.append((nw_x, nw_y))
            res += 1
            
        return res
                
        
    def in_bound(self, x, y, matrix):
        if x < len(matrix) and y < len(matrix[0]):
            return True
        
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": ([[9,9,4],[6,6,8],[2,1,1]]), "expected_output": 4}
    ]
    for test_case in test_cases:
        assert solution.longestIncreasingPath(test_case["input"]) == test_case["expected_output"]