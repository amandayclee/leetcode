class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
       sum_calculate_lst = sum([int(x) for x in list(str(x))])
       remainder = x % sum_calculate_lst
       if (remainder):
           return -1
       else:
           return sum_calculate_lst


if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": 18, "expected_output": 9},
        {"input": 23, "expected_output": -1}
    ]
    for test_case in test_cases:
        assert solution.sumOfTheDigitsOfHarshadNumber(test_case["input"]) == test_case["expected_output"]