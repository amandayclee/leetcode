from typing import List


class Solution:
    def can_ship(self, capacity, weights, days):
        ships = 1
        current_capacity = capacity
        for weight in weights:
            if current_capacity - weight < 0:
                ships += 1
                current_capacity = capacity
            current_capacity -= weight
        return ships <= days
    
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lower_bound, upper_bound = max(weights), sum(weights)
        res = sum(weights)
        
        while lower_bound <= upper_bound:
            capacity = lower_bound + (upper_bound - lower_bound) // 2
            if self.can_ship(capacity, weights, days):
                res = min(res, capacity)
                upper_bound = capacity - 1
            else:
                lower_bound = capacity + 1
        return res
    

if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": [[1,2,3,4,5,6,7,8,9,10], 5], "expected_output": 15}
    ]
    for test_case in test_cases:
        assert solution.shipWithinDays(test_case["input"][0], test_case["input"][1]) == test_case["expected_output"]