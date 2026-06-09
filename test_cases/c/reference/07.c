#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

bool isMatch(char* s, char* p) {
    int m = strlen(s), n = strlen(p);
    bool* prev = calloc(n + 1, sizeof(bool));
    bool* cur = calloc(n + 1, sizeof(bool));
    prev[0] = true;
    for (int j = 1; j <= n; j++) prev[j] = prev[j - 1] && p[j - 1] == '*';
    for (int i = 1; i <= m; i++) {
        cur[0] = false;
        for (int j = 1; j <= n; j++) {
            if (p[j - 1] == '*') cur[j] = prev[j] || cur[j - 1];
            else if (p[j - 1] == '?' || p[j - 1] == s[i - 1]) cur[j] = prev[j - 1];
            else cur[j] = false;
        }
        bool* t = prev; prev = cur; cur = t;
    }
    bool res = prev[n];
    free(prev);
    free(cur);
    return res;
}
