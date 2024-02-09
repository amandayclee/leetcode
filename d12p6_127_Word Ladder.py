from typing import List
import collections

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for asterisk in range(len(word)):
                pattern = word[:asterisk] + '*' + word[asterisk + 1:]
                nei[pattern].append(word)
        
        visited = set([beginWord])
        q = collections.deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for asterisk in range(len(word)):
                    pattern = word[:asterisk] + '*' + word[asterisk + 1:]
                    for neighbor in nei[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
            res += 1
        return 0

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        {"input": (["hit", "cog", ["hot","dot","dog","lot","log","cog"]]), "expected_output": 5}
    ]
    for test_case in test_cases:
        assert solution.ladderLength(test_case["input"][0], test_case["input"][1], test_case["input"][2]) == test_case["expected_output"]