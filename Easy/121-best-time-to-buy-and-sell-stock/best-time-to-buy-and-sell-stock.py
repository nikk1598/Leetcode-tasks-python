class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        curr_min = prices[0]
        for i in range(1, len(prices)):
            ans = max(ans, prices[i] - curr_min)
            curr_min = min(curr_min, prices[i])
        return ans
