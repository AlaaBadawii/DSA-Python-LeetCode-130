def maxProfit(prices: list[int]) -> int:
    """Calculates the maximum profit that can be achieved from
    buying and selling a stock given its prices over time."""
    max_profit = 0
    lowest_price = prices[0]

    for curr_price in prices:
        if curr_price > lowest_price:
            profit = curr_price - lowest_price
            max_profit = max(max_profit, profit)
        else:
            lowest_price = curr_price

    return max_profit
