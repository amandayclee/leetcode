class ListNode:
    
    def __init__(self, key, next=None):
        self.key = key
        self.next = next
        

class MyHashSet:

    def __init__(self, size=10000):
        self.size = size
        self.hash_set = [ListNode(0) for _ in range(self.size)]
    
    def _hash(self, key: int):
        return key % self.size

    def add(self, key: int) -> None:
        index = self._hash(key)
        current_node = self.hash_set[index]
        
        while current_node.next:
            if current_node.next.key == key:
                return
            current_node = current_node.next
        current_node.next = ListNode(key)

    def remove(self, key: int) -> None:
        index = self._hash(key)
        current_node = self.hash_set[index]
        
        while current_node.next:
            if current_node.next.key == key:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def contains(self, key: int) -> bool:
        index = self._hash(key)
        current_node = self.hash_set[index]
        
        while current_node.next:
            if current_node.next.key == key:
                return True
            current_node = current_node.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)