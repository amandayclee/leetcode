from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left, right = 0, n - 1

        while left < n:
            while right > left:
                remain = target - numbers[left]
                print('idx:', left, 'num:', numbers[left], '\nidx:', right, 'num:', numbers[right])

                if numbers[left] + numbers[right] == target:
                    return [left + 1, right + 1]

                if numbers[right] > remain:
                    right -= 1
                else:
                    left += 1

            left += 1

solution = Solution()

print(solution.twoSum([5,25,75], 100))

# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         head, tail = 0, len(numbers) - 1
        
#         while head < tail:
#             s = numbers[head] + numbers[tail]
#             if s == target:
#                 return [head + 1, tail + 1]
#             elif s < target:
#                 head += 1
#             elif s > target:
#                 tail -= 1