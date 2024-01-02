arr = [7,1,5,3,6,4]

# Day 1 = 7 , Day 2 = 1 , Day 3 = 5 , Day 4 = 3


# Maximize the profit when you buy and sell it

# Approach 
max_profit = 0
for j in range(len(arr)):
    if j in [0,1] :
        continue
    remaining_min = min(arr[:j-1])
    profit=abs(arr[j]-remaining_min)
    max_profit= max(profit,max_profit)


print(max_profit)
