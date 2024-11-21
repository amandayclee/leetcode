from heapq import heappop, heappush


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        count = 0
        num = 1
        
        while count < n:
            if self.isUgly(num):
                count += 1
                if count == n:
                    return num
            num += 1
        
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
            
        for factor in [2, 3, 5]:
            while n % factor == 0:
                n //= factor
                
        return n == 1
    
# TC O(n * m * log m) 1 <= n <= 1690 -> TLE
# nth ugly #, m need to check
# SC O(1)

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        seen = {1}
        heap = [1]
        factors = [2, 3, 5]
        
        for _ in range(n - 1):
            curr = heappop(heap)
            
            for factor in factors:
                new_ugly = curr * factor
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heappush(heap, new_ugly)
                    
        return heap[0]
    
# TC O((n - 1) * (log n + 3log n) = O(n log n)
# SC O(n)
