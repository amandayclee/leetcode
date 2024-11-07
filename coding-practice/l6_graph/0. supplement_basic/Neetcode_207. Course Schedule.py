from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisite_adj_list = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:           
            prerequisite_adj_list[course].append(pre)
                    
        visited = set()
        completed = set()
        
        for course in range(numCourses):
            if not self.dfs(course, prerequisite_adj_list, visited, completed):
                return False
        return True
            
    def dfs(self, course, prerequisite_adj_list, visited, completed):
        if course in visited:
            return False # loop
        if course in completed:
            return True
        if prerequisite_adj_list[course] == []:
            completed.add(course)
            return True
        
        visited.add(course)
        
        for pre in prerequisite_adj_list[course]:
            if not self.dfs(pre, prerequisite_adj_list, visited):
                return False

        visited.remove(course)
        completed.add(course)
        
        return True
        
        
# TC O(V + E)
# build adj_list O(V)
# add pre O(E)
# dfs visit vertex + dfs visit edge

# SC O()


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisite_adj_list = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:           
            prerequisite_adj_list[course].append(pre)

        
        for course in range(numCourses):
            if not self.bfs(course, prerequisite_adj_list):
                return False
        return True
            
    def bfs(self, course, prerequisite_adj_list):
        visited = set()
        queue = deque()
        
        visited.add(course)
        queue.append(course)
        
        while queue:
            curr_course = queue.popleft()
            
            for pre in prerequisite_adj_list[curr_course]:
                if course in visited:
                    return False # loop
                if prerequisite_adj_list[course] == []:
                    return True
                
                queue.append(pre)
                visited.add(pre)
        
        return True
        