from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i : i[0])
        res = [intervals[0]]
        
        for start, end in intervals[1:]:
            last_end = res[-1][1]
            
            if start <= last_end:
                res[-1][1] = max(last_end, end)
            else:
                res.append([start, end])
        
        return res
    
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": ([[1,3],[2,6],[8,10],[15,18]]), "expected_output": [[1,6],[8,10],[15,18]]},
        {"input": ([[1,4],[4,5]]), "expected_output": [[1,5]]}
    ]
    for test_case in test_cases:
        print(test_case)
        assert solution.merge(test_case["input"]) == test_case["expected_output"]
