class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        b = prices[0]
        for i in range(1, len(prices)):
            v = prices[i]
            if v < b:
                b = v
            else:
                output = max(v-b, output)
        return output