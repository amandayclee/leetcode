# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

from typing import List

class Solution:
    def reverseString(s: List[str]) -> None:
        head, tail = 0, len(s) - 1

        while head < tail:
            s[head], s[tail] = s[tail], s[head]
            head += 1
            tail -= 1

        return s

print(Solution.reverseString(["H","a","n","n","a","h"]))