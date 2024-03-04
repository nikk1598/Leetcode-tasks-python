class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        i = 0
        j = 0
        count = 1
        ans = 0
        d = {s[0]:1}

        while True:
            if count == j - i + 1:
                ans = max(ans, j-i+1)
                j += 1
                if j >= len(s):
                    break
                if s[j] not in d:
                    d[s[j]] = 1
                else:
                    d[s[j]] += 1
                if d[s[j]] == 1:
                    count += 1
                elif d[s[j]] == 2:
                    count -= 1
                
            else:
                i += 1
                d[s[i-1]] -= 1
                if d[s[i-1]] == 1:
                    count += 1
                elif d[s[i-1]] == 0:
                    count -= 1
            print(i, j, ans)

        return ans
            
 