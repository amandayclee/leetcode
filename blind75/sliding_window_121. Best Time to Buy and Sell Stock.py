from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_cost = prices[0]
        profit = 0


        for i in range(len(prices)):
            min_cost = min(min_cost, prices[i])
            profit = max(prices[i] - min_cost, profit)
        
        return profit
    
# TC O(n)
# SC O(1)