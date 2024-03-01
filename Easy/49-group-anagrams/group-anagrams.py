class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for s in strs:
            s_sorted = ''.join(sorted(s))
            if s_sorted not in d:
                d[s_sorted] = [s]
            else:
                d[s_sorted].append(s)

        res = []
        for key in d.keys():
            res.append(d[key])

        return res