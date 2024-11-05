from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerequisite_adj_list = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:           
            prerequisite_adj_list[course].append(pre)
                    
        visited = set()
        
        for course in range(numCourses):
            if not self.dfs(course, prerequisite_adj_list, visited):
                return False
        return True
            
    def dfs(self, course, prerequisite_adj_list, visited):
        if course in visited:
            return False # loop
        if prerequisite_adj_list[course] == []:
            return True
        
        visited.add(course)
        
        for pre in prerequisite_adj_list[course]:
            if not self.dfs(pre, prerequisite_adj_list, visited):
                return False

        visited.remove(course)
        prerequisite_adj_list[course] = []
        
        return True
        
        
# TC O(V + E)
# build adj_list O(V)
# add pre O(E)
# dfs visit vertex + dfs visit edge

# SC O()
