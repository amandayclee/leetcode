from typing import List
import random


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.quick_select(0, len(points) - 1, k - 1, points)
        return points[:k]

    def distance_squared(self, point):
        x, y = point
        return x * x + y * y

    def quick_select(self, left, right, K, points):
        if left == right:
            return

        pivot_index = random.randint(left, right)
        pivot_index = self.partition(left, right, pivot_index, points)

        if K == pivot_index:
            return
        elif K < pivot_index:
            self.quick_select(left, pivot_index - 1, K, points)
        else:
            self.quick_select(pivot_index + 1, right, K, points)

    def partition(self, left, right, pivot_index, points):
        pivot_distance = self.distance_squared(points[pivot_index])

        points[pivot_index], points[right] = points[right], points[pivot_index]

        store_index = left
        for i in range(left, right):
            i_distance = self.distance_squared(points[i])
            if i_distance < pivot_distance:
                points[store_index], points[i] = points[i], points[store_index]
                store_index += 1

        points[right], points[store_index] = points[store_index], points[right]

        return store_index


solution = Solution()
print(solution.kClosest([[3, 3], [5, -1], [-2, 4]], 2))
