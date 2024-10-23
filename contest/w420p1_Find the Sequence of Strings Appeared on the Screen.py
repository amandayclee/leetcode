from typing import List


class Solution:
    def stringSequence(self, target: str) -> List[str]:
        self.screen = []
        self.idx = -1
        self.temp = ""
        
        for char in target:
            self.press_key1()
            self.screen.append(self.temp)
            while self.temp[self.idx] != char:
                self.press_key2(self.temp[self.idx])
                self.screen.append(self.temp)

        return self.screen
        
    def press_key1(self):
        self.temp += "a"
        self.idx += 1        
        
    def press_key2(self, char):
        after_press = chr(ord(char) + 1)
        self.temp = self.temp[:self.idx] + after_press
        
Solution().stringSequence("abc")