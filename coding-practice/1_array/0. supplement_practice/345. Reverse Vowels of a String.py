class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left, right = 0, len(s) - 1
        vowels = set('aeiouAEIOU')
        
        while left < right:
            while left < right and s[left] not in vowels:
                left += 1
            while left < right and s[right] not in vowels:
                right -= 1
            
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return ''.join(s)
    

if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": "IceCreAm", "expected_output": "AceCreIm"},
        {"input": "leetcode", "expected_output": "leotcede"},
    ]

    for test_case in test_cases:
        input_data = test_case["input"]
        expected_output = test_case["expected_output"]
        assert solution.reverseVowels(input_data) == expected_output, f"Test case failed: {test_case}"
    
    print("All test cases passed!")
    
    # TC O(N)
    # SC O(N) string 轉 list 時