# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return head.next
        
        fast = slow = head
        
        for _ in range(n):
            fast = fast.next
        
        if not fast: # n equals to the length of ll
            return head.next
            
        while fast.next:
            slow = slow.next
            fast = fast.next
            
        slow.next = slow.next.next
        
        return head
        
# TC O(n)
# SC O(1)