def subset(weight,target_sum):
    n =len (weight)
    dp = [[0]*(target_sum+1) for _ in range(n+1)]

    for i in range(1,n+1):
        weit = weight[i-1]
        for w in range(1,target_sum+1):
            if(weit>w):
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-weit]+weit)
    selected_items = []
    i,j =n,target_sum
    while i>0 and j>0:
        if (dp[i][w]!=dp[i-1][w]):
            selected_items.append(weight[i-1])
            w-=weight[i-1]
        i-=1


    return dp[n][target_sum],selected_items

weights = [3, 34, 4, 12, 5, 2]
target_sum = 9

result,items = subset(weights,9)
if(result):
    print("items that can sum up for targeted sum of ",target_sum," are :")
    print(items)
else:
    print("not possible")