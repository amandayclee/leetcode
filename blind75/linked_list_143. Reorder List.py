# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        # find mid
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # give a new access to splitted linked list
        second = slow.next
        slow.next = None # split first half and second half
        first = head
        
        # reverse second half
        prev = None
        curr = second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        second = prev
        
        # combine
        while second:
            first_node = first.next
            second_node = second.next
            
            first.next = second
            second.next = first_node
            
            first = first_node
            second = second_node
            
# TC O(n)
# SC O(1)