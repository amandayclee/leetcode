from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i, len(matrix[i])):
                # print("i", i, "j", j)
                # print("matrix[i][j]", matrix[i][j], "matrix[j][i]", matrix[j][i])

                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(len(matrix)):
            # print("before reverse", matrix[i])
            matrix[i].reverse()
            # print("after reverse", matrix[i])


solution = Solution()
solution.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
