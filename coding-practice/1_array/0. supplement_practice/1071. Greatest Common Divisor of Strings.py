class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # 如果 str1 + str2 和 str2 + str1 不相等，則不可能有 GCD 字串
        if str1 + str2 != str2 + str1:
            return ""
        
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        gcd_len = gcd(len(str1), len(str2))
        # GCD 字串應該是 str1 或 str2 的前 gcd_len 個字元
        return str1[:gcd_len]

solution = Solution()
print(solution.gcdOfStrings("ABCABC", "ABC"))  # Output: "ABC"
print(solution.gcdOfStrings("ABABAB", "ABAB"))  # Output: "AB"
print(solution.gcdOfStrings("LEET", "CODE"))    # Output: ""
