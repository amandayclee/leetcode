class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= (n - 1)
            res += 1            
        return res
    
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": 128, "expected_output": 1},
        {"input": 11, "expected_output": 3}
    ]
    for test_case in test_cases:
        assert solution.hammingWeight(test_case["input"]) == test_case["expected_output"]