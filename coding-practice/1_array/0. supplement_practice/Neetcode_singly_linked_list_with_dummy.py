from typing import List


class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node
        
class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        curr = self.head.next
        i = 0
        
        while curr:
            if i == index:
                return curr.val
            i += 1
            curr = curr.next
        return -1
    
    def insertHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node
    
    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        
    def remove(self, index: int) -> bool:
        curr = self.head # because we have to find the node before the one we want to remove
        i = 0
        
        while i < index and curr:
            i += 1
            curr = curr.next
        
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False
    
    def getValues(self) -> List[int]:
        curr = self.head.next
        res = []
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res