from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjacency = self.build_graph(edges)
        return self.has_path(adjacency, source, destination, set())
        
    # build a adjacency list
    def build_graph(self, edges):
        graph = {}
        for edge in edges:
            u, v = edge
            if u not in graph:
                graph[u] = []
            graph[u].append(v)
            if v not in graph:
                graph[v] = []
            graph[v].append(u)
        return graph

    # dfs
    def has_path(self, adjacency, source, destination, visited):
        if source == destination:
            return True
        if source in visited:
            return False
        visited.add(source)
        for neighbour in adjacency[source]:
            if self.has_path(adjacency, neighbour, destination, visited):
                return True
        return False

        
if __name__ == "__main__":
    solution = Solution()
    
    test_cases = [
        {"input": (6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5), "expected_output": False}
    ]
    for test_case in test_cases:
        assert solution.validPath(test_case["input"][0], test_case["input"][1], test_case["input"][2], test_case["input"][3]) == test_case["expected_output"]