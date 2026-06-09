#include <stdlib.h>
#include <string.h>
#include <limits.h>

char* minWindow(char* s, char* t) {
    int need[128] = {0}, win[128] = {0};
    int required = 0;
    for (int i = 0; t[i]; i++) {
        if (need[(unsigned char)t[i]] == 0) required++;
        need[(unsigned char)t[i]]++;
    }
    int sl = strlen(s);
    int have = 0, left = 0, bestLen = INT_MAX, bestStart = 0;
    for (int right = 0; right < sl; right++) {
        unsigned char c = s[right];
        win[c]++;
        if (need[c] > 0 && win[c] == need[c]) have++;
        while (have == required) {
            if (right - left + 1 < bestLen) { bestLen = right - left + 1; bestStart = left; }
            unsigned char lc = s[left];
            win[lc]--;
            if (need[lc] > 0 && win[lc] < need[lc]) have--;
            left++;
        }
    }
    char* res;
    if (bestLen == INT_MAX) {
        res = malloc(1);
        res[0] = '\0';
    } else {
        res = malloc(bestLen + 1);
        memcpy(res, s + bestStart, bestLen);
        res[bestLen] = '\0';
    }
    return res;
}
