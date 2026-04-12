

# input = Array
# ouput = max profit by buying on previous day adn selling on next day
# two pointers
# left and right pointers - left at start and right at one step forward
# if right -left < 0 increment left by one step cause it means that was not the best price to
# buy and right ++
# if right - left > 0 move right forward
# if rigth - left >0  store max

class Solution:
    def maxProfit(self, prices):
        left = 0
        right = left + 1
        max_profit = 0

        while right < len(prices):
            checkSub = prices[right] - prices[left]

            if prices[left] < prices[right]:
                max_profit = max(max_profit, checkSub)
            else:
                left = right
            right += 1
        
        return max_profit





sol=Solution()
prices = [7,1,5,3,6,4]

print(sol.maxProfit(prices))

# Time Complexity - BigO(n)
# Space Complexity - BigO(1)