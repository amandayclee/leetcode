class DoublyLinkedListNode:
    
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}
        
        self.head = DoublyLinkedListNode(None, "head")
        self.tail = DoublyLinkedListNode(None, "tail")
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert(self, node):
        prev, nxt = self.tail.prev, self.tail
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self, key: int) -> int:
        if key in self.hash_map:
            self.remove(self.hash_map[key])
            self.insert(self.hash_map[key])
            return self.hash_map[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            self.remove(self.hash_map[key])
        self.hash_map[key] = DoublyLinkedListNode(key, value)
        self.insert(self.hash_map[key])
        
        if len(self.hash_map) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.hash_map[lru.key]
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)