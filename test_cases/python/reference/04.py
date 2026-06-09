from collections import Counter

def findSubstring(s, words):
    if not s or not words:
        return []
    word_len = len(words[0])
    total_len = word_len * len(words)
    need = Counter(words)
    result = []
    for i in range(len(s) - total_len + 1):
        seen = Counter(s[j:j + word_len] for j in range(i, i + total_len, word_len))
        if seen == need:
            result.append(i)
    return result
