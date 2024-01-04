class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        aliceSum = sum(aliceSizes)
        bobSum = sum(bobSizes)
        aliceSizesSet = set(aliceSizes)

        for num in bobSizes:
            """
            The element, x, that we are looking for in AliceSizesSet
            should equal the sums of AliceSum and BobSum when replacing x --> num in AliceSizes
            and replacing  num --> x in BobSizes.
        
            bobSum - num + x = aliceSum - x + num
            ## 2x = aliceSum - bobSum + 2*num
            ## x = (aliceSum - bobSum + 2*num) / 2
            """
            x = (aliceSum - bobSum + 2*num) // 2
            if x in aliceSizesSet:
                return [x, num]

