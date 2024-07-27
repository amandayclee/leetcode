from typing import List
import collections

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, i):
        if (self.parent[i] == i):
            return i
        else:
            return self.find(self.parent[i])
    
    def union(self, rank, i,j):
        irep = self.parent.find(i)
        jrep = self.parent.find(j)

        self.parent[irep] = jrep
        
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int: