class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(val="head")
        self.tail = Node(val="tail")
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def add_in_the_end(self, new_node):
        self.cache[new_node.key] = new_node
        cur_last_node = self.tail.prev
        
        cur_last_node.next = new_node
        new_node.prev = cur_last_node
        
        self.tail.prev = new_node
        new_node.next = self.tail
        
    def remove_from_the_beginnig(self):
        del self.cache[self.head.next.key]
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        
    def update_to_newest(self, node):
        if node == self.tail.prev:
            return
        
        prev_node = node.prev
        prev_node.next = node.next
        node.next.prev = prev_node
        
        self.add_in_the_end(node)


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.update_to_newest(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.update_to_newest(self.cache[key])
        else:
            self.add_in_the_end(Node(key, value))
        
            if len(self.cache) > self.capacity:
                self.remove_from_the_beginnig()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == "__main__":
    test_cases = [
        {"input": [["LRUCache","put","put","get","put","put","get"], [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]], "expected_output": [None,None,None,2,None,None,-1]}
    ]
    for test_case in test_cases:
        actions, params = test_case["input"]
        expected_output = test_case["expected_output"]
        result = []
        
        solution = None  # 初始化 LRUCache 的變數
        
        for action, param in zip(actions, params):
            if action == "LRUCache":
                solution = LRUCache(*param)  # 初始化 LRUCache
                result.append(None)
            elif action == "put":
                result.append(solution.put(*param))
            elif action == "get":
                result.append(solution.get(*param))
        
        assert result == expected_output

