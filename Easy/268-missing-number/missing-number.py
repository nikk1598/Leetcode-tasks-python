class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = set()
        for x in range(0, len(nums)+1):
            s.add(x)
                
        for x in s:
            if x not in nums:
                return x
        