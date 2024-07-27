# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.


class Solution:
    def compute_lps_array(self, pattern):
        """ Compute the longest prefix-suffix (LPS) array. """
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

    def strStr(self, haystack: str, needle: str) -> int:
        text = haystack
        pattern = needle
        lps_table = self.compute_lps_array(pattern)
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
                    
        return -1


solution = Solution()
print(solution.strStr("mississippi", "issip"))