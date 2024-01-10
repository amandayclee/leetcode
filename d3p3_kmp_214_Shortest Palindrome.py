class Solution:
    def shortestPalindrome(self, s: str) -> str:
        new_s = s + "#" + s[::-1]
        lps = self.build_lps(new_s)
        longest_palindrome_length = lps[-1]
        print('new_s', new_s)
        print('lps', lps)
        print('s', s)
        print('s[longest_palindrome_length:]', s[longest_palindrome_length:])
        print('s[longest_palindrome_length:][::-1]', s[longest_palindrome_length:][::-1])
        print('s[longest_palindrome_length:][::-1] + s', s[longest_palindrome_length:][::-1] + s)
        return s[longest_palindrome_length:][::-1] + s

    def build_lps(self, s: str) -> list:
        lps = [0] * len(s)
        length = 0
        i = 1

        while i < len(s):
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            elif length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

        return lps


solution = Solution()
print(solution.shortestPalindrome("aacecaaa"))
