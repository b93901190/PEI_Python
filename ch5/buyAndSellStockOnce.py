def buySellStockOnce(prices):
    minPriceSoFar, maxProfit = float('inf'), 0.0
    for price in prices:
        maxProfitToday = price - minPriceSoFar
        maxProfit = max(maxProfit, maxProfitToday)
        minPriceSoFar = min(minPriceSoFar, price)
    return maxProfit

A = [310,310,275,295,260,270,290,230,230,230]
print  'max profit ', buySellStockOnce(A)
