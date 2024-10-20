class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.length = 0
        
    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        currr = self.head
        for _ in range(index):
            curr = curr.next
        return curr. val
    
    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        
    def insertTail(self, val:int) -> None:
        new_node = ListNode(val)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def remove(self, index: int) -> bool:
        if index < 0 or index >= self.length:
            return False
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
                
            curr.next = curr.next.next
            self.length -= 1
            return True