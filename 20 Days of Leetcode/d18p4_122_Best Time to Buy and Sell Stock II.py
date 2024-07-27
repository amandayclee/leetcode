from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        dp = {}
        # have stock / cannot buy but can rest or sell / 1 / True
        # not have stock / cannot sell but can rest or buy  / 0 / False
        def maxProfitFromDay(i, have_stock):
            if i == len(prices):
                return 0
            
            if (i, have_stock) in dp:
                return dp[(i, have_stock)]
            
            if have_stock == 1:
                dp[(i, have_stock)] = max(
                    maxProfitFromDay(i + 1, 0) + prices[i], # sell
                    maxProfitFromDay(i + 1, 1) # rest
                )
            else:
                dp[(i, have_stock)] = max(
                    maxProfitFromDay(i + 1, 1) - prices[i], # buy
                    maxProfitFromDay(i + 1, 0) # rest
                )
                
            return dp[(i, have_stock)]
        return maxProfitFromDay(0, False)