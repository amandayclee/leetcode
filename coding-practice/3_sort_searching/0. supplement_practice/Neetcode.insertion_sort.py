from typing import List


class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

lass Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        if not pairs:
            return pairs
            
        result = [pairs[:]]
        
        for i in range(1, len(pairs)):
            j = i - 1

            while j >= 0 and pairs[j].key > pairs[j + 1].key:
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
                j -= 1
            
            result.append(pairs[:])

        return result
    
print(Solution().insertionSort([Pair(5, "apple"), Pair(2, "banana"), Pair(9, "cherry")]))