from collections import defaultdict
from heapq import heapify, heappop, heappush
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = defaultdict(int)
        for task in tasks:
            counter[task] += 1
        
        heap = [(-count, task) for task, count in counter.items()]
        heapify(heap)
        
        cd_task = [] # (count, task, available_time)
        current_time = 0
        
        while heap or cd_task:
            while cd_task and cd_task[0][2] <= current_time:
                count, task, _ = cd_task.pop(0)
                if count < 0:
                    heappush(heap, (count, task))

            if heap:
                count, task = heappop(heap)
                if count + 1 < 0:
                    cd_task.append((count + 1, task, current_time + n + 1))
                    
            current_time += 1
            
        return current_time