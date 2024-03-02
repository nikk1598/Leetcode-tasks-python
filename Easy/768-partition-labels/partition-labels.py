class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = [i]
            else:
                d[s[i]].append(i)
        
        events = []
        for char in d.keys():
            events.append((d[char][0], 0))
            events.append((d[char][-1], 1))
        events.sort()

        count = 0
        pos = 0
        ans = []
        for event in events:
            if event[1] == 0:
                count += 1
                if count == 1:
                    pos = event[0]
            else:
                count -= 1
                if count == 0:
                    ans.append(event[0]-pos+1)
        return ans
