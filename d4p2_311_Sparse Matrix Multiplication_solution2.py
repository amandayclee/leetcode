from typing import List


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        matrix1_row_idx = len(mat1)
        matrix1_col_idx = len(mat1[0])  # is also matrix2_row_idx
        matrix2_col_idx = len(mat2[0])
        result = [[0] * matrix1_row_idx] * matrix2_col_idx
        
        # compressed sparse rows
        non_zero_mat1 = {}
        non_zero_mat2 = {}
        
        for i in range(matrix1_row_idx):
            for j in range(matrix1_col_idx):
                if mat1[i][j] != 0:
                    if i not in non_zero_mat1:
                        non_zero_mat1[i] = {}
                    non_zero_mat1[i][j] = mat1[i][j]
                                               
        for j in range(matrix1_col_idx):
            for l in range(matrix2_col_idx):
                if mat2[j][l] != 0:
                    if j not in non_zero_mat2:
                        non_zero_mat2[j] = {}
                    non_zero_mat2[j][l] = mat2[j][l]
        
        for mat1_row in non_zero_mat1:
            for mat1_col in non_zero_mat1[i]:
                if mat1_col in non_zero_mat2:  # as a row idx
                    for mat2_col in non_zero_mat2[mat1_col]:
                        result[mat1_row][mat1_col] = non_zero_mat1[mat1_row][mat1_col] * non_zero_mat2[mat1_col][mat2_col]
        
        return result


solution = Solution()
solution.multiply([[1, 0, 0], [-1, 0, 3]], [[7, 0, 0], [0, 0, 0], [0, 0, 1]])
