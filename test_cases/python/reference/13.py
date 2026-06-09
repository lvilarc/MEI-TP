def numDistinct(s, t):
    dp = [0] * (len(t) + 1)
    dp[0] = 1
    for ch in s:
        for j in range(len(t) - 1, -1, -1):
            if t[j] == ch:
                dp[j + 1] += dp[j]
    return dp[-1]
