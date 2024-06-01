class Solution:
    def compressedString(self, word: str) -> str:
        if not word:
            return ""

        idx_check = 1
        count = 1
        compress = ""

        while idx_check < len(word):
            if word[idx_check] == word[idx_check - 1]:
                count += 1
                if count == 9:
                    compress += str(count) + word[idx_check - 1]
                    count = 0
            else:
                compress += str(count) + word[idx_check - 1]
                count = 1
            idx_check += 1
        
        compress += str(count) + word[idx_check - 1]

        return compress
        
solution = Solution()
print(solution.compressedString("aaaaaaaaaaaaaabb"))