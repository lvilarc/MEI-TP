#include <stdlib.h>
#include <string.h>

int* findSubstring(char* s, char** words, int wordsSize, int* returnSize) {
    int sl = strlen(s);
    int cap = 16, cnt = 0;
    int* res = malloc(sizeof(int) * cap);
    *returnSize = 0;
    if (wordsSize == 0) return res;
    int wl = strlen(words[0]);
    int total = wl * wordsSize;
    if (total > sl) return res;
    int* used = malloc(sizeof(int) * wordsSize);
    for (int i = 0; i + total <= sl; i++) {
        memset(used, 0, sizeof(int) * wordsSize);
        int matched = 0;
        for (int j = 0; j < wordsSize; j++) {
            char* seg = s + i + j * wl;
            int found = -1;
            for (int w = 0; w < wordsSize; w++) {
                if (!used[w] && strncmp(seg, words[w], wl) == 0) { found = w; break; }
            }
            if (found == -1) break;
            used[found] = 1;
            matched++;
        }
        if (matched == wordsSize) {
            if (cnt == cap) { cap *= 2; res = realloc(res, sizeof(int) * cap); }
            res[cnt++] = i;
        }
    }
    free(used);
    *returnSize = cnt;
    return res;
}
