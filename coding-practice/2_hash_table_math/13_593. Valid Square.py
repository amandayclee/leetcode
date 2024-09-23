from typing import List


class Solution:
    def validSquare(
        self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]
    ) -> bool:

        points = [p1, p2, p3, p4]
        distances = []

        # Compute all pairwise squared distances
        for i in range(4):
            for j in range(i + 1, 4):
                distances.append(self.squared_distance(points[i], points[j]))

        # Sort distances to simplify counting
        distances.sort()

        # Check the conditions for a valid square
        # There should be exactly two distinct distances: sides and diagonals
        # The smaller distance (sides) should appear 4 times
        # The larger distance (diagonals) should appear 2 times
        return (
            len(set(distances)) == 2
            and distances.count(distances[0]) == 4
            and distances.count(distances[4]) == 2
        )

    def squared_distance(self, p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
    
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": ([0,0],[1,1],[1,0],[0,1]), "expected_output": True},
        {"input": ([0,0],[1,1],[1,0],[0,12]), "expected_output": False},
        {"input": ([1,0],[-1,0],[0,1],[0,-1]), "expected_output": True}
    ]

    for test_case in test_cases:
        input_data = test_case["input"]
        expected_output = test_case["expected_output"]
        assert solution.valid_square(*input_data) == expected_output, f"Test case failed: {test_case}"
    
    print("All test cases passed!")