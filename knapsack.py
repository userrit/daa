

# List of items: (weight, value)
items = [
    (3, 10),
    (5, 4),
    (6, 9),
    (2, 11)
]

def knapsack(items,capacity):
    n = len(items)
    dp = [[0]*(capacity+1) for _ in range(n+1)]     # --> capacity+1 and n+1

    for i in range(1, n+1):                # n+1
        weight,value = items[i-1]
        for w in range(1,capacity+1):     #capacity+1  .....all  for loops n+1
            if(weight>w):
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight]+value)

    selected_items=[]
    i =n
    while i>0:
        if (dp[i][w]!=dp[i-1][w]):
            selected_items.append(items[i-1])
            w-=items[i-1][0]
        i-=1

    return dp[n][capacity], selected_items

cap = 7
val,item = knapsack(items,cap)

print("max value is ",val)
print("items are : ",item)