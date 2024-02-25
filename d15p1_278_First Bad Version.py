# The isBadVersion API is already defined for you.

class Solution:
    def firstBadVersion(self, n: int, bad_version) -> int:
        def isBadVersion(version: int) -> bool:
            return version >= bad_version
        
        start, end = 1, n
        
        while start < end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1              
        return start

if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": ([5, 2]), "expected_output": 2}
    ]
    for test_case in test_cases:
        assert solution.firstBadVersion(test_case["input"][0], test_case["input"][1]) == test_case["expected_output"]