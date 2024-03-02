class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        events = []
        for interval in intervals:
            events.append((interval[0], 0))
            events.append((interval[1], 1))
        
        events.sort()
        count = 0
        i = 0
        ans = []
        for event in events:
            if event[1] == 0:
                count += 1
                if count == 1:
                    i = event[0]
            else:
                count -= 1
                if count == 0:
                    ans.append([i, event[0]])

        return ans
