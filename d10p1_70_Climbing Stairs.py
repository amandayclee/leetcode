class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 0 or n == 1:
            return 1
        
        return self.climbStairs(n-2) + self.climbStairs(n - 1)