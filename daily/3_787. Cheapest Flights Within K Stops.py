from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        prices = [float("inf")] * n
        prices[src] = 0
        
        for i in range(k + 1):
            temp_prices = prices.copy()
            
            for source, destination, price in flights:
                if prices[source] == float("inf"):
                    continue
                elif prices[source] + price < temp_prices[destination]:
                    temp_prices[destination] = prices[source] + price
            prices = temp_prices
            
        return -1 if prices[dst] == float("inf") else prices[dst]
    
print(Solution().findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3, 1))
print(Solution().findCheapestPrice(2, [[1,0,5]], 0, 1, 1))
print(Solution().findCheapestPrice(7, [[0,3,7],[4,5,3],[6,4,8],[2,0,10],[6,5,6],[1,2,2],[2,5,9],[2,6,8],[3,6,3],[4,0,10],[4,6,8],[5,2,6],[1,4,3],[4,1,6],[0,5,10],[3,1,5],[4,3,1],[5,4,10],[0,1,6]], 2, 4, 1))