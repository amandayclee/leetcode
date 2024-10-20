# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(-1)
        merged_lst = dummy_node
        
        while list1 and list2:
            if list1.val < list2.val:
                merged_lst.next = list1
                list1 = list1.next
            else:
                merged_lst.next = list2
                list2 = list2.next
            merged_lst = merged_lst.next
            
        merged_lst.next = list1 if list1 else list2
        
        return dummy_node.next