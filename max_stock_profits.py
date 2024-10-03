class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # create a variable to hold the profit amount
        profit = 0

        # created a new sorted list of the price listing to look for best buys and best sells
        buy_sell_list = sorted(prices, reverse = True)
        # and also check if the prices of the days are in descending order, then we cannot make any profit
        if prices == buy_sell_list:
            return profit

        # initialize the buy price to the first element
        buy = prices[0]

        # go through the list of prices starting at the second element
        for i in range(1, len(prices)):
            # if the new pricing is lower than our current buy pricing, then make it the new buy
            if prices[i] < buy:
                buy = prices[i]
            # otherwise, if the current profit is greater than the max profit we have (held in the profit variable)
            # update the profits to the new greatest number
            elif prices[i] - buy > profit:
                profit = prices[i] - buy

        return profit