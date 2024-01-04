class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceSum = sum(aliceSizes)
        bobSum = sum(bobSizes)
        aliceSizesSet = set(aliceSizes)

        for num in bobSizes:
            ## bobSum - num + x = aliceSum - x + num
            ## 2x = aliceSum - bobSum + 2*num
            ## x = (aliceSum - bobSum + 2*num) / 2
            x = (aliceSum - bobSum + 2*num) // 2
            if x in aliceSizesSet:
                return [x, num]

