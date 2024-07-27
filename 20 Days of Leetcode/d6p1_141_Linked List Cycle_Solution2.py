# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited_nodes = set()
        current_node = head
        while current_node:
            if current_node in visited_nodes:
                return True
            visited_nodes.add(current_node)
            current_node = current_node.next
        
        return False
            

nodes1 = [ListNode(3), ListNode(2), ListNode(0), ListNode(-4)]
for i in range(len(nodes1) - 1):
    nodes1[i].next = nodes1[i + 1]
nodes1[-1].next = nodes1[1]
solution1 = Solution()
print(solution1.hasCycle(nodes1[0])) 