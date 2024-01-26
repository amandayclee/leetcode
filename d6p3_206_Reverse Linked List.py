from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # recursive
        if not head:
            return None
        if not head.next:
            return head
        
        reversed_node = self.reverseList(head.next)
        current_node = reversed_node
        while current_node.next:
            current_node = current_node.next
        current_node.next = head
        head.next = None
        
        return reversed_node
    
nodes1 = [ListNode(1), ListNode(2), ListNode(3), ListNode(4)]
for i in range(len(nodes1) - 1):
    nodes1[i].next = nodes1[i + 1]
solution = Solution()
solution.reverseList(nodes1[0])