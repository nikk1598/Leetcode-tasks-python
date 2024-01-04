class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        for num in bobSizes:
            ## bobSum - num + x = aliceSum - x + num
            ## 2x = aliceSum - bobSum + 2*num
            ## x = (aliceSum - bobSum + 2*num) / 2
            x = (sum(aliceSizes) - sum(bobSizes) + 2*num) // 2
            if x in set(aliceSizes):
                return [x, num]

