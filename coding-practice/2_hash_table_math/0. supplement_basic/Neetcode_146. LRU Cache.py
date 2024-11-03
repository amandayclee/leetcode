class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_tail(self, node):
        """在尾部前添加節點"""
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
            
    def remove_node(self, node):
        """刪除指定節點"""
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def move_to_tail(self, node):
        """將節點移到尾部（最近使用）"""
        self.remove_node(node)
        self.add_to_tail(node)
        
    def remove_head(self):
        """移除頭部節點（最久未使用）"""
        if self.head.next != self.tail:
            node = self.head.next
            self.remove_node(node)
            return node
        return None
          
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> Node
        self.dll = DoublyLinkedList()

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # 更新位置
            self.dll.move_to_tail(node)
            return node.value
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 更新現有節點
            node = self.cache[key]
            node.value = value
            self.dll.move_to_tail(node)
        else:
            # 新增節點
            node = Node(key, value)
            self.cache[key] = node
            self.dll.add_to_tail(node)
            
            # 檢查容量
            if len(self.cache) > self.capacity:
                # 移除最久未使用的節點
                lru_node = self.dll.remove_head()
                del self.cache[lru_node.key]
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)