class ListNode:
    
    def __init__(self, key=-1, value=-1, next=None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.hash_table = [ListNode() for i in range(self.size)]
        
    def _hash(self, key):
        return key % self.size
        
    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        
        current_node = self.hash_table[index]
        while current_node.next:
            if current_node.next.key == key:
                current_node.next.value = value
                return
            current_node = current_node.next
        current_node.next = ListNode(key, value)

    def get(self, key: int) -> int:
        index = self._hash(key)
        
        current_node = self.hash_table[index].next
        while current_node and current_node.key != key:
            current_node = current_node.next
        if current_node:
            return current_node.value
        return -1
                

    def remove(self, key: int) -> None:
        index = self._hash(key)
        
        current_node = self.hash_table[index]

        while current_node.next and current_node.next.key != key:
            current_node = current_node.next
        if current_node and current_node.next:
            current_node.next = current_node.next.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
