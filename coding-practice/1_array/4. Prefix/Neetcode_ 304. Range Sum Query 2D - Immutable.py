from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sum_matrix = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        
        for row in range(ROWS):
            prefix = 0
            for col in range(COLS):
                prefix += matrix[row][col]
                above = self.sum_matrix[row][col + 1]
                self.sum_matrix[row + 1][col + 1] = prefix + above

# TC O(m*n)
# SC O(m*n)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottom_right = self.sum_matrix[row2 + 1][col2 + 1]
        above = self.sum_matrix[row1][col2 + 1]
        left = self.sum_matrix[row2 + 1][col1]
        top_left = self.sum_matrix[row1][col1]
        
        return bottom_right - above - left + top_left
        
# TC O(1)
# SC O(1)

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)