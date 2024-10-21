class ListNode:
    def __init__(self, val, prev_node=None, next_node=None):
        self.val = val
        self.prev = prev_node
        self.next = next_node

class MyLinkedList:

    def __init__(self):
        self.left = ListNode(-1)
        self.right = ListNode(-1)
        self.left.next = self.right
        self.right.prev = self.left
        
    def get(self, index: int) -> int:
        curr = self.left.next
        while curr and index > 0:
            curr = curr.next
            index -= 1
            
        if curr and curr != self.right and index == 0:
            return curr.val
        
        return -1
            
    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.prev = self.left
        new_node.next = self.left.next
        self.left.next.prev = new_node
        self.left.next = new_node
        

    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.prev = self.right.prev
        new_node.next = self.right
        self.right.prev.next = new_node
        self.right.prev = new_node


    def addAtIndex(self, index: int, val: int) -> None:
        new_node = ListNode(val)
        curr = self.left.next
        
        while curr != self.right and index > 0:
            curr = curr.next
            index -= 1
        
        if curr and index == 0:
            new_node.prev = curr.prev
            new_node.next = curr
            curr.prev.next = new_node
            curr.prev = new_node
            

    def deleteAtIndex(self, index: int) -> None:
        curr = self.left.next
        
        while curr != self.right and index > 0:
            curr = curr.next
            index -= 1
            
        if curr and curr != self.right and index == 0:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
    

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)