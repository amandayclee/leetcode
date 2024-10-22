from typing import List


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while students and sandwiches:
            if sandwiches[0] == students[0]:
                students.pop(0)
                sandwiches.pop(0)        
            else:
                if sandwiches[0] not in students:
                    break
                students.append(students.pop(0))
            
        return len(students)

# O(n^2) while loop + pop
# O(n) need to shift the array for pop

from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = deque(students)    # O(n)
        sandwiches = deque(sandwiches)  # O(n)
        
        count = 0
        while students and count < len(students):
            if students[0] == sandwiches[0]:
                students.popleft()
                sandwiches.popleft()
                count = 0
            else:
                students.append(students.popleft())
                count += 1
        
        return len(students)
    
# O(n) while loop
# O(n) for dequeu space

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = [students.count(0), students.count(1)]
        
        for sandwich in sandwiches:
            if count[sandwich] > 0:
                count[sandwich] -= 1
            else:
                return sum(count)
        return 0
    
# O(n) for loop
# O(1) constant space