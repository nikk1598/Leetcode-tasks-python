class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        d = {}
        for char in s1:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1

        i = 0
        j = -1
        zero_count = 0
        while j < len(s2)-1:
            j += 1
            if s2[j] in d:
                d[s2[j]] -= 1
                if d[s2[j]] == 0:
                    zero_count += 1
                elif d[s2[j]] == -1:
                    zero_count -= 1
            
            if j >= len(s1):
                i += 1
                if s2[i-1] in d:
                    d[s2[i-1]] += 1
                    if d[s2[i-1]] == 0:
                        zero_count += 1
                    elif d[s2[i-1]] == 1:
                        zero_count -= 1
            
            if zero_count == len(d):
                return True

        return False
                        


