class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, int(n**0.5 + 1)):
            if is_prime[i]:
                for j in range(i * i, n, i):
                    is_prime[j] = False
        
        return sum(is_prime)
    
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": 10, "expected_output": 4},
        {"input": 0, "expected_output": 0},
        {"input": 1, "expected_output": 0}
    ]

    for test_case in test_cases:
        input_data = test_case["input"]
        expected_output = test_case["expected_output"]
        assert solution.countPrimes(input_data) == expected_output, f"Test case failed: {test_case}"
    
    print("All test cases passed!")