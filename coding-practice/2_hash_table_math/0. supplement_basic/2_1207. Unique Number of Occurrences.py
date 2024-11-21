from collections import defaultdict
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = {}
        
        for ele in arr:
            occurences[ele] = occurences.get(ele, 0) + 1
        
        temp = set()
        for occurence in occurences.values():
            if occurence in temp:
                return False
            temp.add(occurence)
        return True
    
# TC O(n + k)
# SC O(k + k)


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurences = defaultdict(int)
        
        for ele in arr:
            occurences[ele] += 1
        
        return len(occurences.values()) == len(set(occurences.values()))