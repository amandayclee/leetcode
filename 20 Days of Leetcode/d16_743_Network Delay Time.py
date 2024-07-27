from typing import List
import sys
import heapq
# test

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            graph[u].append((v, w))
            
        distances = {i: sys.maxsize for i in range(1, n + 1)}
        distances[k] = 0
        
        heap = [(0, k)]  # path from source to target, target node
        while heap:
            current_distance, current_node = heapq.heappop(heap)
            if current_distance > distances[current_node]:
                continue
            
            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))
                    
        max_distance = max(distances.values())
        return max_distance if max_distance < sys.maxsize else -1
    
solution = Solution()
solution.networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)