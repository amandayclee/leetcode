class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        # 兩個整數 n, k
        # 0 秒 最開始的 array [1, 1, 1, 1]
        # 1 秒 再過一秒是前面的加總 [1, 2, 3, 4]
        # 2 秒 [1, 3, 6, 10]
        # ...
        # k (5) 秒 [1, 6, 21, 56]
        
        # n, k 必大於 0
        memo = {}
        memo[0] = [1] * n

        def helper(n, k, memo):
            if k == 0:
                return memo[0]
            
            if k in memo:
                return memo[k]
            
            prev = helper(n, k - 1, memo)
            memo[k] = [0] * n
            for i in range(n):
                if i == 0:
                    memo[k][i] = 1
                else:
                    memo[k][i] = memo[k][i - 1] + prev[i]
            
            return memo[k]
        
        return helper(n, k, memo)[-1]
        
if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        {"input": ([4, 2]), "expected_output": 10},
    ]
    for test_case in test_cases:
        assert solution.valueAfterKSeconds(test_case["input"][0], test_case["input"][1]) == test_case["expected_output"]
        
        

# class Solution:
#     def valueAfterKSeconds(self, n: int, k: int) -> int:
#         MOD = 10**9 + 7  # 取模值以避免大数溢出

#         # 初始化第0秒的数组
#         dp = [1] * n

#         for second in range(1, k + 1):
#             new_dp = [1] * n
#             for i in range(1, n):
#                 new_dp[i] = (new_dp[i - 1] + dp[i]) % MOD
#             dp = new_dp
        
#         return dp[-1]