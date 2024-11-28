class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # a circle 360 degree
        # an hour 360 / 12 = 30 degree
        # a min 360 / 12 / 5 = 6 degree
        
        # 12: 30
        # min will be 30 * 6 = 180
        # hour will be 30 * (0 + 30 / 60) = 15
        # degree will be min - hour = 180 - 15 = 165
        
        # 3: 30
        # min will be 30 * 6 = 180
        # hour will be 30 * (3 + 30 / 60) = 105
        # degree will be min - hour = 180 - 105 = 75
        
        # 3: 15
        # min will be 15 * 6 = 90
        # hour will be 30 * (3 + 30 / 60) = 105
        # degree will be 105 - 90 = 15
        
        degree_pre_hour = 360 / 12
        degree_pre_min = 360 / 12 / 5
        
        hour_cal = degree_pre_hour * (hour % 12 + minutes / 60)
        min_cal = degree_pre_min * minutes
        
        same_side = abs(hour_cal - min_cal)
        diff_side = 360 - same_side
        
        return min(same_side, diff_side)
    
        # 1: 57
        # min will be 6 * 57 = 342
        # hour will be 30 * (1 + 57 / 60) = 58.5
        # 360 - 342 + 58. 5