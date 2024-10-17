class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        vowels = set('aeiou')
        n = len(word)
        count = 0
        
        for i in range(n):
            seen_vowels = set()
            consonant_count = 0
            for j in range(i, n):
                if word[j] in vowels:
                    seen_vowels.add(word[j])
                else:
                    consonant_count += 1
                    
                if len(seen_vowels) == 5 and consonant_count == k:
                    count += 1
                elif consonant_count > k:
                    break
                
        return count