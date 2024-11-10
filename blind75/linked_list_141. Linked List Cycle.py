# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        
        if not fast or not fast.next:
            return False
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
            if fast == slow:
                return True
        
        return False