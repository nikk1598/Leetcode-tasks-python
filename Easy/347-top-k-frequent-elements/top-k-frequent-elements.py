class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1

        freq = sorted([(d[x], x) for x in d.keys()])[::-1]
        return [x[1] for x in freq[:k]]

