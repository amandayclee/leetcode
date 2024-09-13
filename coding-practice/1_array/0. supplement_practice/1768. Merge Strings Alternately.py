class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        count = 0
        combined = ""

        while count < min(len(word1), len(word2)):
            if count < len(word1) > 0:
                combined += word1[count]
            if count < len(word2) > 0:
                combined += word2[count]
            count += 1
        
        combined += (word1[count:] + word2[count:])

        return combined

if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": ("abc", "pqr"), "expected_output": "apbqcr"},
        {"input": ("ab", "pqrs"), "expected_output": "apbqrs"},  # Additional test case
        {"input": ("abcd", "pq"), "expected_output": "apbqcd"}   # Additional test case
    ]

    for test_case in test_cases:
        input_data = test_case["input"]
        expected_output = test_case["expected_output"]
        assert solution.mergeAlternately(*input_data) == expected_output, f"Test case failed: {test_case}"
    
    print("All test cases passed!")

# TC O(n)
# SC O(n)