"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visited = {}
        return self.dfs_traverse(node, visited)
        
        
    def dfs_traverse(self, node, visited):
        if node in visited:
            return visited[node]
        
        new_node = Node(node.val)
        visited[node] = new_node
        
        for neighbor in node.neighbors:
            new_node.neighbors.append(self.dfs_traverse(neighbor, visited))
            
        return new_node
    
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        visited = {}
        queue = deque()
        
        queue.append(node)
        visited[node] = Node(node.val)
        
        while queue:
            old_node = queue.popleft()
                
            for neighbor in old_node.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                
                new_node = visited[old_node]    
                new_node.neighbors.append(visited[neighbor])
                        
        return visited[node]