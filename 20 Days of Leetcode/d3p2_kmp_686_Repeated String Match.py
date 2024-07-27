class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        text = a
        pattern = b
        
        times = (len(pattern) - 1) // len(text) + 1  # Ceiling.
        lps_table = self.compute_lps_array(pattern)  # build kmp pattern table

        for i in range(0, 2):
            index = self.search(lps_table, text * (times + i), pattern)

            if index is not None:
                return times + i

        return -1

    def search(self, lps_table, text, pattern):
        text_idx, pattern_idx = 0, 0

        while text_idx < len(text):
            if text[text_idx] == pattern[pattern_idx]:
                text_idx += 1
                pattern_idx += 1

            if pattern_idx == len(pattern):
                return text_idx - pattern_idx
            elif text_idx < len(text) and text[text_idx] != pattern[pattern_idx]:
                if pattern_idx != 0:
                    pattern_idx = lps_table[pattern_idx - 1]
                else:
                    text_idx += 1
        return None

    def compute_lps_array(self, pattern):
        """Compute the longest prefix-suffix (LPS) array."""
        length = 0  # length of the longest prefix suffix
        check_idx = 1
        lps_table = [0] * len(pattern)

        while check_idx < len(pattern):
            if pattern[length] == pattern[check_idx]:
                length += 1
                lps_table[check_idx] = length
                check_idx += 1
            else:
                if length != 0:
                    length = lps_table[length - 1]
                else:
                    lps_table[check_idx] = 0
                    check_idx += 1
        return lps_table


solution = Solution()
print(solution.repeatedStringMatch("a", "aa"))
