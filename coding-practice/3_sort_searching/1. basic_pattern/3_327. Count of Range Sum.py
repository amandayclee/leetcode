from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix_sum = [0]
        for n in nums:
            prefix_sum.append(prefix_sum[-1] + n)

        return self._mergesort(prefix_sum, lower, upper, 0, len(prefix_sum) - 1)

    def _mergesort(
        self, prefix_sum: List[int], lower: int, upper: int, left: int, right: int
    ) -> int:
        if left == right:
            return 0

        mid = (left + right) // 2
        count = self._mergesort(prefix_sum, lower, upper, left, mid) + self._mergesort(
            prefix_sum, lower, upper, mid + 1, right
        )

        i = j = mid + 1
        for left_value in prefix_sum[left : mid + 1]:
            while i <= right and prefix_sum[i] - left_value < lower:
                i += 1
            while j <= right and prefix_sum[j] - left_value <= upper:
                j += 1
            count += j - i

        prefix_sum[left : right + 1] = sorted(prefix_sum[left : right + 1])
        return count
    
    
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": ([-2,5,-1], -2, 2), "expected_output": 3},
        {"input": ([0], 0, 0), "expected_output": 1},
    ]

    for test_case in test_cases:
        input_data = test_case["input"]
        expected_output = test_case["expected_output"]
        assert solution.countRangeSum(*input_data) == expected_output, f"Test case failed: {test_case}"
    
    print("All test cases passed!")