class Solution:
    def mySqrt(self, x: int) -> int:
        start, end = 0, x
        
        while start <= end:
            mid = start + ((end - start) // 2)
            square = mid * mid
            
            if square > x:
                end = mid - 1
            elif square < x:
                # print('start: ' + str(start) + ' end: ' + str(end) + ' mid: ' + str(mid))
                start = mid + 1
            else:
                return mid
        return end

if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": 8, "expected_output": 2}
    ]
    for test_case in test_cases:
        assert solution.mySqrt(test_case["input"]) == test_case["expected_output"]