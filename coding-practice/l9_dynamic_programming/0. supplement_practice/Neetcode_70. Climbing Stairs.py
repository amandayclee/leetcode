class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
            
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

# TC O(2^n) cannot pass TLE
# SC O(log n)

class Solution:
    def climbStairs(self, n: int) -> int:
        self.cache = {}
        return self.dfs(n)
        
    def dfs(self, n):
        if n == 0 or n == 1:
            return 1
        
        if n in self.cache:
            return self.cache[n]
        
        self.cache[n] = self.dfs(n - 1) + self.dfs(n - 2)
        
        return self.cache[n]

# TC O(n)
# SC O(n)

class Solution:
    def climbStairs(self, n:int) -> int:
        if n == 0 or n == 1:
            return 1
        
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
    
# TC O(n)
# SC O(n)

class Solution:
    def climbStairs(self, n:int) -> int:
        if n == 0 or n == 1:
            return 1
        
        dp = [1, 1]
        i = 2
        
        while i <= n:
            temp = dp[1]
            dp[1] = dp[0] + dp[1]
            dp[0] = temp
            i += 1
            
        return dp[1]
    
# TC O(n)
# SC O(1)