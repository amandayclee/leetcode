class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo = {}
        return self.climbStairs_helper(n)
        
    def climbStairs_helper(self, n):
        if n == 0 or n == 1:
            return 1
        
        if n in self.memo:
            return self.memo[n]
        
        self.memo[n] = self.climbStairs_helper(n - 1) + self.climbStairs_helper(n - 2)
        return self.memo[n]
    
print(Solution().climbStairs(3))