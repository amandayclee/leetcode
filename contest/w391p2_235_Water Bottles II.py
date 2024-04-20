class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        empty_bottles = 0
        total_bottles_drunk = 0
        
        while numBottles > 0:
            total_bottles_drunk += numBottles
            empty_bottles += numBottles
            numBottles = 0
            while empty_bottles >= numExchange:
                empty_bottles -= numExchange
                numBottles += 1
                numExchange += 1

        return total_bottles_drunk

if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": [13, 6], "expected_output": 15},
        {"input": [10, 3], "expected_output": 13}
    ]
    for test_case in test_cases:
        assert solution.maxBottlesDrunk(test_case["input"][0], test_case["input"][1]) == test_case["expected_output"]
