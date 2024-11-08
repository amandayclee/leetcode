# to build adjacency list from 
from collections import deque


edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]

# with hash map
adjList = {}

for src, dst in edges:
    if src not in adjList:
        adjList[src] = []
    if dst not in adjList:
        adjList[dst] = []
    adjList[src].append(dst)
    
    
# we wanted to count the number of paths that lead from a source to destination.
# backtracking

def dfs(node, target, adjList, visit):
    if node in visit:
        return 0
    
    if node == target:
        return 1
    
    count = 0
    visit.add(node)
    for neighbor in adjList[node]:
        count += dfs(neighbor, target, adjList, visit)
    visit.remove(node)
    
    return count

# N: # of edges each vertax has
# V: height of the tree
# TC O(N^V) worst case O(V^V)
# SC O(V) 

# our goal is to find the shortest path from node to target
def bfs(node, target, adjList):
    length = 0
    visit = set()
    visit.add(node)
    queue = deque()
    queue.append(node)
    
    while queue:
        for i in range(len(queue)):
            curr = queue.popleft()
            if curr == target:
                return length
            
            for neighbor in adjList[curr]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    queue.append(neighbor)
        length += 1
    return length

# V: the number of vertices  
# E: is the number of edges
# TC O(V+E)
# SC O(V)
# visit # V
# queue # V
# others constant

class Graph:
    
    def __init__(self):
        self.adj_list = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj_list:
            self.adj_list[src] = []
        if dst not in self.adj_list:
            self.adj_list[dst] = []
        if dst not in self.adj_list[src]:
            self.adj_list[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj_list or dst not in self.adj_list:
            return False
        
        self.adj_list[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        visit = set()
        return self.dfs_helper(src, dst, visit) > 0
    
    def dfs_helper(self, node, target, visit):
        if node in visit:
            return 0

        if node == target:
            return 1

        count = 0
        visit.add(node)

        for neighbor in self.adj_list[node]:
            count += self.dfs_helper(neighbor, target, visit)

        visit.remove(node)

        return count