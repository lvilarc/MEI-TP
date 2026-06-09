from collections import defaultdict, deque

def findLadders(beginWord, endWord, wordList):
    words = set(wordList)
    if endWord not in words:
        return []
    layer = {beginWord: [[beginWord]]}
    while layer:
        next_layer = defaultdict(list)
        for word, paths in layer.items():
            if word == endWord:
                return paths
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nxt = word[:i] + c + word[i + 1:]
                    if nxt in words:
                        next_layer[nxt] += [path + [nxt] for path in paths]
        words -= set(next_layer.keys())
        layer = next_layer
    return []
