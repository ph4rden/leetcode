from typing import List
'''
    1. traverse prices array
    2. use two ptrs (sliding window) to keep track of the max profit 
    3. go until right ptr reach end of array
    4. return max profit
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0

        while r < len(prices): 
            if prices[l] < prices[r]: 
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else: 
                # price at right ptr is less than price at left
                l = r
            r += 1
        return max_profit

sol = Solution()
print(sol.maxProfit([7,1,5,3,6,4]))