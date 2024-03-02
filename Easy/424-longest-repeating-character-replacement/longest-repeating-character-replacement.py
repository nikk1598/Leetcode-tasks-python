class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        j = 0
        d = {s[0] : 1}
        max_freq = 1
        ans = 1

        while True:
            if j-i+1-max_freq <= k:
                ans = max(j-i+1, ans)
                j += 1
                if j >= len(s):
                    break
                if s[j] in d:
                    d[s[j]] += 1
                else:
                    d[s[j]] = 1
                max_freq = max(max_freq, d[s[j]])
            else:
                d[s[i]] -= 1
                i += 1
                max_freq = max([d[x] for x in d.keys()])
        return ans
            


