from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda i : i[0])
        max_same_meeting_room = 0
        buffer = []  # used for check past nodes
        
        for interval in intervals:
            buffer.append(interval)
            intervals_to_remove = []
            buffer_idx = len(buffer) - 1
            while buffer_idx >= 0:
                current_start, check_past_end = interval[0], buffer[buffer_idx][1]
                
                if current_start >= check_past_end:  # not overlap
                    intervals_to_remove.append(buffer[buffer_idx])
                buffer_idx -= 1
                    
            for interval_to_remove in intervals_to_remove:
                buffer.remove(interval_to_remove)
            
            max_same_meeting_room = max(max_same_meeting_room, len(buffer))
            
        
        return max_same_meeting_room