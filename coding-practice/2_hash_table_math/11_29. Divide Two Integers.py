class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Check if the result should be positive or negative
        result_is_positive = (dividend < 0) == (divisor < 0)

        # If the dividend is the smallest possible number and the divisor is -1,
        # the result would be too big, so we return the biggest possible number
        if dividend == -(2**31) and divisor == -1:
            return 2**31 - 1

        # Make both numbers positive
        dividend = abs(dividend)
        divisor = abs(divisor)
        final_quotient = 0

        # These lists will keep track of multiples of the divisor
        divisor_multiples = []
        quotients_for_multiples = []
        current_quotient = 1

        # Keep doubling the divisor and store the results
        while dividend >= divisor:
            divisor_multiples.append(divisor)
            quotients_for_multiples.append(current_quotient)

            divisor += divisor
            current_quotient += current_quotient

        # Subtract the largest possible multiples of the divisor from the dividend
        for idx, divisor_multiple in enumerate(reversed(divisor_multiples)):
            if divisor_multiple > dividend:
                continue

            final_quotient += quotients_for_multiples[len(quotients_for_multiples) - 1 - idx]
            dividend -= divisor_multiple

        # If the result should be positive, return the result
        if result_is_positive:
            return final_quotient

        # If the result should be negative, return the negative result
        return -final_quotient

if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": (13, 3), "expected_output": 4},
        {"input": (7, -3), "expected_output": -2},
        {"input": (10, 3), "expected_output": 3},
        {"input": (1, 1), "expected_output": 1},
    ]

    for test_case in test_cases:
        input_data = test_case["input"]
        expected_output = test_case["expected_output"]
        assert solution.divide(*input_data) == expected_output, f"Test case failed: {test_case}"
    
    print("All test cases passed!")