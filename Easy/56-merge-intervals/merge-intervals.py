class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        events = []
        for interval in intervals:
            events.append([interval[0], 0])
            events.append([interval[1], 1])
        
        events.sort()
        start_pos = 0
        count = 0
        ans = []

        for event in events:
            if event[1] == 0:
                count += 1
                if count == 1:
                    start_pos = event[0]
            else:
                count -= 1
                if count == 0:
                    ans.append([start_pos, event[0]])

        return ans
