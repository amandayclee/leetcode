from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        current_node, prev_current = head, dummy
        length = 0
        
        # calculate how many nodes in the linked list
        while current_node:
            length += 1
            current_node = current_node.next
            
        while length >= k:
            current_node = prev_current.next  # means head for the first loop
            current_next_node = current_node.next
            for _ in range(1, k):
                current_node.next = current_next_node.next
                current_next_node.next = prev_current.next
                prev_current.next = current_next_node
                current_next_node = current_node.next
            prev_current = current_node
            length -= k
        
        return dummy.next