# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

nodes1 = [ListNode(3), ListNode(2), ListNode(0), ListNode(-4)]
for i in range(len(nodes1) - 1):
    nodes1[i].next = nodes1[i + 1]
nodes1[-1].next = nodes1[1]
solution1 = Solution()
print(solution1.hasCycle(nodes1[0])) 