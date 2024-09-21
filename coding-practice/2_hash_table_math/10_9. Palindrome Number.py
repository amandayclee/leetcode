class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10
        
        return x == reverted_number or x == reverted_number // 10
        
        

if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": 1221, "expected_output": True},
        {"input": -121, "expected_output": False},
        {"input": 10, "expected_output": False}
    ]

    for test_case in test_cases:
        input_data = test_case["input"]
        expected_output = test_case["expected_output"]
        assert solution.isPalindrome(input_data) == expected_output, f"Test case failed: {test_case}"
    
    print("All test cases passed!")