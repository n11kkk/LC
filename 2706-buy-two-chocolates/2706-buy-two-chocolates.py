class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        ans = money
        # low1 = float('inf')
        # low2 = float('inf')
        # for i in range(len(prices)):
        #     if(prices[i]<low1):
        #         low1=i
        # for i in range(len(prices)):
        #     if(prices[i]<low2 and i!=low1):
        #         low2=i
        # if(money-prices[low1]-prices[low2]>=0):
        #     ans = money-prices[low1]-prices[low2]
        # return ans
        sorted_prices = sorted(prices)
        print(sorted_prices)
        if(sorted_prices[0]+sorted_prices[1]<=money):
            ans = money - sorted_prices[0]-sorted_prices[1]
        return ans
            