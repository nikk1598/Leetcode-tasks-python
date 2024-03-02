class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        i = 0
        j = 0
        ans = 0
        while j < len(prices)-1:
            if prices[j] > prices[j+1]:
                ans += prices[j] - prices[i]
                j += 1
                i = j
            elif prices[j] <= prices[j+1]:
                j += 1
        
        ans += prices[j] - prices[i]
        return ans
                


