class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = dict()
        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]] = [1, i]
            else:
                count[s[i]][0] += 1
                
        for x in count:
            if count[x][0] == 1:
                return count[x][1]
        return -1