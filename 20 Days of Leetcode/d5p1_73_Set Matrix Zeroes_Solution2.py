from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        row_zero = False

        # First pass to mark rows and columns that need to be set to zero
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    if i > 0:
                        matrix[i][0] = 0
                    else:
                        row_zero = True

        # Second pass to set zeros except the first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0

        # Set the first row and column to zero if needed
        if matrix[0][0] == 0:
            for i in range(m):
                matrix[i][0] = 0
        if row_zero:
            for j in range(n):
                matrix[0][j] = 0
    
    
# solution = Solution()
# solution.setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])