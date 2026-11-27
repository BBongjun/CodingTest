dp = [[1,0],
      [0,1]]

for i in range(2, 41):
    count_0 = dp[i-1][0] + dp[i-2][0]
    count_1 = dp[i-1][1] + dp[i-2][1]

    dp.append([count_0, count_1])


num_test = int(input())

for _ in range(num_test):
    n = int(input())
    print(dp[n][0], dp[n][1])