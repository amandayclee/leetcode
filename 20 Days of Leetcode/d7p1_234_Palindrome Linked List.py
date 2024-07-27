from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find mid point
        slow, fast = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next  # slow will stop at the mid point
            
        # reverst the second helf list
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow  # prev will stop at the last reversed node
            slow = temp
            
        # chech palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
    
    