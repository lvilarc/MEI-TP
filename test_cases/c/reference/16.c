#include <stdlib.h>
#include <string.h>

static int diffByOne(const char* a, const char* b) {
    int d = 0;
    for (int i = 0; a[i]; i++) {
        if (a[i] != b[i]) { d++; if (d > 1) return 0; }
    }
    return d == 1;
}

int ladderLength(char* beginWord, char* endWord, char** wordList, int wordListSize) {
    int* used = calloc(wordListSize, sizeof(int));
    char** queue = malloc(sizeof(char*) * (wordListSize + 1));
    int qh = 0, qt = 0;
    queue[qt++] = beginWord;
    int level = 1;
    while (qh < qt) {
        int sz = qt - qh;
        for (int s = 0; s < sz; s++) {
            char* cur = queue[qh++];
            if (strcmp(cur, endWord) == 0) { free(used); free(queue); return level; }
            for (int w = 0; w < wordListSize; w++) {
                if (!used[w] && diffByOne(cur, wordList[w])) {
                    used[w] = 1;
                    queue[qt++] = wordList[w];
                }
            }
        }
        level++;
    }
    free(used);
    free(queue);
    return 0;
}
