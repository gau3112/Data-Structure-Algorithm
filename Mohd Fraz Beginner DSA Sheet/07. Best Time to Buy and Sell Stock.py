def maximumProfit(prices):
    min = prices[0]
    max_profit = 0
    for i in range(len(prices)):
        if prices[i]<min:
            min = prices[i]
        if prices[i]-min >max_profit:
            max_profit = prices[i]-min
    return max_profit
