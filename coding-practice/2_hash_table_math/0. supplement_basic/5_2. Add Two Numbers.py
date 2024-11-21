# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_node1 = l1
        curr_node2 = l2

        num1 = num2 = 0
        times = 1
        
        while curr_node1:
            num1 += curr_node1.val * times
            curr_node1 = curr_node1.next
            times *= 10
        
        times = 1    
        while curr_node2:
            num2 += curr_node2.val * times
            curr_node2 = curr_node2.next
            times *= 10
        
        add_up = str(num1 + num2)
        dummy = ListNode(0)
        head = dummy
            
        for i in range(len(add_up) - 1, -1, -1):
            head.next = ListNode(int(add_up[i]))
            head = head.next
            
        return dummy.next
            
# TC O(n + m)
# SC O(n + m)

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            
            total = x + y + carry
            carry = total // 10
            
            curr.next = ListNode(total % 10)
            curr = curr.next
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next

# TC O(max(n, m))    
# SC O(max(n, m))

# didn't think of dealing sum while traversing