def brute_force(n):
    if n <= 1:
        return n
    return brute_force(n - 1) + brute_force(n - 2)

def memoization(n, cache):
    if n <= 1:
        return n
    if n in cache:
          return cache[n]

    cache[n] = memoization(n - 1, cache) + memoization(n - 2, cache)
    
    return cache[n]

def tabulation(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

def dp(n):
    if n <= 1:
        return n

    dp = [0, 1]
    i = 2
    while i <= n:
        temp = dp[1]
        dp[1] = dp[0] + dp[1]
        dp[0] = temp
        i += 1

    return dp[1]