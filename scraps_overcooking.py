# maxProfit

mid_price = (min_price + max_price) / 2

        # create a new list of potential profits (no need to account for negative profits)
        # there won't be a point where all profits are negative bc we already checked for descending order
        # go through the list and calculate positive profits starting at the maximum pricing until we hit the mid pricing
        
        i = -1                   # current index in the sorted pricing list
        count = 0                # number of times that pricing shows up in the list
        large_price = buy_sell_list[i]      # starting max price we'll search for
        while (large_price > mid_price):
            count = prices.count(large_price)
            index_list.append(0)
            
            for j in count:
                # get the index of the pricing
                index = prices.index(large_price)

                # check the numbers before this number to find the min 
                # if there are more than one instance of this number, check the list between the last instance and this current instance
                min_substring = min(prices[index_list[-1]:index)

                # add it to the index list
                index_list.append(index)

                # calculate the profit
                profit = large_price - min_substring

                # add it to the profits list
                profit_list.append(profit)

                # pop the number
                prices.pop(index)
            
            # add the numbers 
            for k in count:


        
        while (i < days):
            sell = prices[i]    # current sell price

            # if the buy price is higher than the sell price, just skip
            if buy > sell:
                continue

        

days = len(prices)      # how many days we're looking through
 
buy = prices[0]         # current buy price
        # get the index and price of the minimum buy price
        buy = buy_sell_list[-1]
        buy_idx = prices.index(buy)

        # get the index and price of the maximum sell price
        
        sell_idx = prices.index(sell)

        # if the buy pricing occurs before the sell pricing, then return the profit
        if buy_idx < sell_idx:
            profit = sell - buy
            
            