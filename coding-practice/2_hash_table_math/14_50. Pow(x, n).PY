class Solution:
    def myPow(self, x: float, n: int) -> float:
        # x^0 = 1
        res = 1
        
        if n < 0:
            n = -n
            x = 1 / x
            
        while n > 0:
            if n % 2 == 1:
                # If n is odd, multiply result by current x
                res *= x
            # Square the base
            x *= x
            # Divide n by 2 (integer division)
            n //= 2
                
        return res
    
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": (2.00000, 10), "expected_output": 1024.00000},
        {"input": (2.10000, 3), "expected_output": 9.26100},
        {"input": (2.00000, -2), "expected_output": 0.25000},
    ]

    for test_case in test_cases:
        input_data = test_case["input"]
        expected_output = test_case["expected_output"]
        result = solution.myPow(*input_data)
        assert abs(result - expected_output) < 1e-5, f"Test case failed: {test_case}, got {result} instead of {expected_output}"
    
    print("All test cases passed!")
