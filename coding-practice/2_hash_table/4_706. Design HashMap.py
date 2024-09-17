class ListNode:
    
    def __init__(self, key=-1, val=-1, next=None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.size = 1000
        # dummy node for every index
        self.hash_table = [ListNode() for _ in range(self.size)]
        
    def _hash(self, key):
        return key % len(self.hash_table)
    
    def put(self, key: int, value: int) -> None:
        current_node = self.hash_table[self._hash(key)]
        while current_node.next:
            if current_node.next.key == key:
                current_node.next.val = value
                return
            current_node = current_node.next
        current_node.next = ListNode(key, value)

    def get(self, key: int) -> int:
        # skip dummy node
        current_node = self.hash_table[self._hash(key)].next
        while current_node:
            if current_node.key == key:
                return current_node.val
            current_node = current_node.next
        return -1

    def remove(self, key: int) -> None:
        current_node = self.hash_table[self._hash(key)]
        while current_node.next and current_node.next.key != key:
            current_node = current_node.next
        if current_node and current_node.next:
            current_node.next = current_node.next.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)