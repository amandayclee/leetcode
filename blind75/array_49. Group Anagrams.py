from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        freq = defaultdict(list)
        
        for i in range(len(strs)): # O(n)
            count = [0] * 26
            
            for j in strs[i]: # O(k)
                idx = ord(j) - ord('a')
                count[idx] += 1
            
            freq[tuple(count)].append(strs[i])
            
        # result = []
        # for key in freq.keys():
        #     result.append(freq[key])
            
        # return result
        
        return list(freq.values())
    
# TC O(n*m)
# SC O(n*m) n 個長度為 m 的字