class Node:
    def __init__(self, key, value):
        # we don't have key because we only need count
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add_node_in_count(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        
    def remove_node_in_count(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        
    def remove_if_too_many_nodes(self):
        node_need_to_delete = self.head.next
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        return node_need_to_delete
                    
    
class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count_cache = {} # for count -> linked list
        self.node_cache = {}  # for key -> value
        self.key_count_cache = {} # for key -> count
        self.min_count = 0
    
    def update_count(self, key):
        count = self.key_count_cache.get(key, 0)
        self.key_count_cache[key] = count + 1
        if count in self.count_cache:
            self.count_cache[count].remove_node_in_count(self.node_cache[key])
            # if this count linked list is empty
            if (self.count_cache[count].head.next == self.count_cache[count].tail):
                if count == self.min_count:
                    self.min_count += 1
                del self.count_cache[count]
                
        if count + 1 not in self.count_cache:
            self.count_cache[count + 1] = DoublyLinkedList()
        
        self.count_cache[count + 1].add_node_in_count(self.node_cache[key])
            

    def get(self, key: int) -> int:
        if key not in self.node_cache:
            return -1
        self.update_count(key)
        return self.node_cache[key].value
        
    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.node_cache:
            # key already exist, then update value and key count + 1
            self.node_cache[key].value = value
            self.update_count(key)
            return
        
        if len(self.node_cache) == self.capacity:
            least_frequenct_list = self.count_cache[self.min_count]
            node_need_to_delete = least_frequenct_list.remove_if_too_many_nodes()
            del self.node_cache[node_need_to_delete.key]
            del self.key_count_cache[node_need_to_delete.key]
        
        new_node = Node(key, value)
        self.node_cache[key] = new_node
        self.update_count(key)
        self.min_count = 1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)