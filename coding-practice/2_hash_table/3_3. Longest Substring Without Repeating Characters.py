# sliding window + hashset

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        result = 0
        seen = set()
        
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            
            seen.add(s[right])
            result = max(result, right - left + 1)
            
        return result
    
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": ("abcabcbb"), "expected_output": 3},
        {"input": ("bbbbb"), "expected_output": 1},
        {"input": ("pwwkew"), "expected_output": 3}
    ]

    for test_case in test_cases:
        input_data = test_case["input"]
        expected_output = test_case["expected_output"]
        assert solution.lengthOfLongestSubstring(input_data) == expected_output, f"Test case failed: {test_case}"
    
    print("All test cases passed!")