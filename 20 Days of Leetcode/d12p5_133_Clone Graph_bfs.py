import collections

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None
        root = node
        seen = set()
        
        q = collections.deque([root])
        mapping = dict()

        while q:
            node = q.popleft()

            if node in seen:
                continue
            
            seen.add(node)
            mapping[node] = Node(node.val)
            
            for n in node.neighbors:
                q.append(n)
        
        q = collections.deque([root])
        seen = set()
        while q:
            node = q.popleft()
            if node in seen:
                continue
                
            seen.add(node)
            
            new_node = mapping[node]
            
            for n in node.neighbors:
                q.append(n)
                new_node.neighbors.append(mapping[n])
                
        

        return mapping[root]


if __name__ == "__main__":
    solution = Solution()

    # Test case
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    # Clone the graph
    cloned_node = solution.cloneGraph(node1)

    # Assert statements
    assert cloned_node.val == 1
    assert cloned_node.neighbors[0].val == 2
    assert cloned_node.neighbors[1].val == 4
    assert cloned_node.neighbors[0].neighbors[1].val == 3