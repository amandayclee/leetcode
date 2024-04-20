from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        
        min_price = [0] * len(prices)
        max_profit = [0] * len(prices)
        
        min_price[0] = prices[0]
        max_profit[0] = 0
        
        for i in range(1, len(prices)):
            min_price[i] = min(min_price[i - 1], prices[i])
            max_profit[i] = max(max_profit[i - 1], prices[i] - min_price[i - 1])
            
        return max_profit[len(prices) - 1]
    
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": [7,1,5,3,6,4], "expected_output": 5},
        {"input": [7,6,4,3,1], "expected_output": 0}
    ]
    for test_case in test_cases:
        assert solution.maxProfit(test_case["input"]) == test_case["expected_output"]