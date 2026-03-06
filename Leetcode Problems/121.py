"given a list of prices for a stock on a given day, where the ith index represents the price of the stock at the ith day. You have to return the maximum profit achieveable, and 0 if no profit is achievable."
prices = [7,6,4,3,1]
# brute force solution
profit = 0
for i in range(len(prices)):
    buy = i
    for j in range(i+1,len(prices)):
        profit = max(prices[j]-prices[buy],profit)
print(profit)
# time limit exceeded : Time complexity : O(n2), space complexity : O(1)

# optimal solution : Kadane's algorithm
buy = prices[0]
profit = 0
for i in range(1,len(prices)):
    buy = min(buy,prices[i])
    profit = max(profit,prices[i]-buy)
print(profit)