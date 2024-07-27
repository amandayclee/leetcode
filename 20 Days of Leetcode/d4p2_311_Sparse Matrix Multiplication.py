from typing import List


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        print(self.matrix_multiply(mat1, mat2))
            
    def matrix_multiply(self, a, b):
        c = []
        for matrix1_row_idx in range(0, len(a)):
            temp = []
            for matrix2_col_idx in range(0, len(b[0])):
                s = 0
                for matrix1_col_idx in range(0, len(a[0])):
                    s += (
                        a[matrix1_row_idx][matrix1_col_idx]
                        * b[matrix1_col_idx][matrix2_col_idx]
                    )
                temp.append(s)
            c.append(temp)
        return c


solution = Solution()
solution.multiply([[1, 0, 0], [-1, 0, 3]], [[7, 0, 0], [0, 0, 0], [0, 0, 1]])
