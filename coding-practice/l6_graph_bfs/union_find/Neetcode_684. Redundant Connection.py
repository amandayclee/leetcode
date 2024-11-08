from collections import defaultdict
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for u, v in edges:
            visited = set()
            
            if self.dfs(u, v, visited, graph):
                return [u, v]
            
            graph[u].append(v)
            graph[v].append(u)
    
    def dfs(self, source, target, visited, graph):
        if source == target:
            return True
        
        visited.add(source)
        
        for neighbor in graph[source]:
            if neighbor not in visited:
                if self.dfs(neighbor, target, visited, graph):
                    return True
        
        return False