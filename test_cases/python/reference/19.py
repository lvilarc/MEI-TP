from functools import lru_cache

def wordBreak(s, wordDict):
    words = set(wordDict)
    @lru_cache(None)
    def dfs(i):
        if i == len(s):
            return ['']
        out = []
        for j in range(i + 1, len(s) + 1):
            word = s[i:j]
            if word in words:
                for tail in dfs(j):
                    out.append(word if not tail else word + ' ' + tail)
        return out
    return dfs(0)
