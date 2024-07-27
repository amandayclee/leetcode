class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.end_of_word = False
        
class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word: str) -> None:
        current_node = self.root
        
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.end_of_word = True
        

    def search(self, word: str) -> bool:
        current_node = self.root
        
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.end_of_word

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        
        for char in prefix:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)