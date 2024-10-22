class ListNode:
    def __init__(self, val, prev_node=None, next_node=None):
        self.val = val
        self.prev = prev_node
        self.next = next_node

class Deque:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        if self.head.next == self.tail:
            return True
        return False

    def append(self, value: int) -> None:
        new_node = ListNode(value)
        last_node = self.tail.prev
        last_node.next = new_node

        new_node.prev = last_node
        new_node.next = self.tail

        self.tail.prev = new_node

    def appendleft(self, value: int) -> None:
        new_node = ListNode(value)
        first_node = self.head.next
        new_node.next = first_node
        new_node.prev = self.head
        self.head.next = new_node
        first_node.prev = new_node


    def pop(self) -> int:
        if self.isEmpty():
            return -1
        last_node = self.tail.prev
        value = last_node.val
        remain_node = last_node.prev
        remain_node.next = self.tail
        self.tail.prev = remain_node

        return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        first_node = self.head.next
        value = first_node.val
        remain_node = first_node.next
        self.head.next = remain_node
        remain_node.prev = self.head

        return value
        
