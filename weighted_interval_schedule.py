def weighted_interval_scheduling(requests):
    # Sort the requests based on finish times
    requests.sort(key=lambda x: x[1])

    n = len(requests)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        current_request = requests[i - 1] 
        start, finish, profit = current_request

        # Find the latest non-overlapping request
        j = i - 1
        while j >= 1 and requests[j - 1][1] > start:
            j -= 1

        # Calculate maximum profit
        dp[i] = max(profit + dp[j], dp[i - 1])

    return dp[n]

# List of requests: (start, finish, profit)
requests = [
    (1, 2, 100),
    (2, 5, 200),
    (3, 6, 300),
    (4, 8, 400),
    (5, 9, 500),
    (6, 10, 100)
]

max_profit = weighted_interval_scheduling(requests)
print("Maximum Profit:", max_profit)
