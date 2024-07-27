# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n <= 0 or n == 1:
#             return 1
        
#         return self.climbStairs(n-2) + self.climbStairs(n - 1)

class Solution:
    def climbStairs(self, n: int) -> int:        
        memo = {}
        return self.helper(n, memo)
    
    def helper(self, n, memo):
        if n == 0 or n == 1:
            return 1
        if n not in memo:
            memo[n] = self.helper(n-1, memo) + self.helper(n-2, memo)
        return memo[n]