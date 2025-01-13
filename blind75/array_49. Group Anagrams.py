from collections import defaultdict
from typing import Dict, List, Tuple

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]

        temp = {}

        for word in strs:
            key = self.get_frequency(word)
            if key not in temp:
                temp[key] = []
            temp[key].append(word)
            
        return list(temp.values())

    def get_frequency(self, word: str) -> Tuple[Dict[str, int]]:
        frequency = [0] * 26

        for char in word:
            char_idx = ord(char) - ord('a')
            frequency[char_idx] += 1
        
        return tuple(frequency)

if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        # {"input": (["eat","tea","tan","ate","nat","bat"]), "expected_output": [["bat"],["nat","tan"],["ate","eat","tea"]]},
        {"input": ([""]), "expected_output": [[""]]},
        {"input": (["a"]), "expected_output": [["a"]]},
    ]
    for test_case in test_cases:
        assert solution.groupAnagrams(test_case["input"]) == test_case["expected_output"]
        

