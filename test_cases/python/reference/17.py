def minCut(s):
    n = len(s)
    cut = list(range(-1, n))
    for i in range(n):
        r = 0
        while i - r >= 0 and i + r < n and s[i - r] == s[i + r]:
            cut[i + r + 1] = min(cut[i + r + 1], cut[i - r] + 1)
            r += 1
        r = 0
        while i - r >= 0 and i + r + 1 < n and s[i - r] == s[i + r + 1]:
            cut[i + r + 2] = min(cut[i + r + 2], cut[i - r] + 1)
            r += 1
    return cut[n]
