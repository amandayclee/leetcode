from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zero_idx = []
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_idx.append([i, j])
                    
        for row, col in zero_idx:
            # col
            for i in range(n):
                matrix[row][i] = 0
            # row
            for j in range(m):
                matrix[j][col] = 0
    
    
# solution = Solution()
# solution.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])