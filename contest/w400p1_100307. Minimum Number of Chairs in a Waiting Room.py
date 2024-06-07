class Solution:
    def minimumChairs(self, s: str) -> int:
        current_chairs = 0
        max_chairs = 0

        for char in s:
            if char == 'E':
                current_chairs += 1
                max_chairs = max(max_chairs, current_chairs)
            elif char == 'L':
                current_chairs -= 1

        return max_chairs
    
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        {"input": ("ELELEEL"), "expected_output": 2},
        {"input": ("ELEELEELLL"), "expected_output": 3},
    ]
    for test_case in test_cases:
        assert solution.minimumChairs(test_case["input"]) == test_case["expected_output"]