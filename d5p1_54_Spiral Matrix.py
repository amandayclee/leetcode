# from typing import List


# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         top, bottom = 0, len(matrix)
#         left, right = 0, len(matrix[0])
#         result = []

#         while left < right and top < bottom:
#             for i in range(left, right):
#                 result.append(matrix[top][i])
#             top += 1

#             for i in range(top, bottom):
#                 result.append(matrix[i][right - 1])
#             right -= 1

#             if not (left < right and top < bottom):
#                 break

#             for i in range(right - 1, left - 1, -1):
#                 result.append(matrix[bottom - 1][i])
#             bottom -= 1

#             for i in range(bottom - 1, top - 1, -1):
#                 result.append(matrix[i][left])
#             left += 1

#         return result

from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    l, r, u, d = 0, len(matrix[0]) - 1, 0, len(matrix) - 1

    res = []

    while l < r and u < d:
        for i in range(l, r + 1):
            res.append(matrix[u][i])

        u += 1

        for i in range(u, d + 1):
            res.append(matrix[i][r])

        r -= 1

        for i in range(r, l - 1, -1):
            res.append(matrix[d][i])

        d -= 1

        for i in range(d, u - 1, -1):
            res.append(matrix[i][l])

        l += 1

    if l == r:
        for i in range(u, d + 1):
            res.append(matrix[i][l])
    elif u == d:
        for i in range(l, r + 1):
            res.append(matrix[u][i])

    return res


spiralOrder([[1, 2, 3]])
