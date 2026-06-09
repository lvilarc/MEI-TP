#include <string.h>
#include <stdbool.h>

static signed char memo[31][31][32]; /* -1 unknown, 0 false, 1 true */

static bool helper(const char* s1, const char* s2, int i, int j, int len) {
    if (memo[i][j][len] != -1) return memo[i][j][len];
    bool res = false;
    if (strncmp(s1 + i, s2 + j, len) == 0) {
        res = true;
    } else {
        int cnt[26] = {0};
        for (int k = 0; k < len; k++) { cnt[s1[i + k] - 'a']++; cnt[s2[j + k] - 'a']--; }
        bool ok = true;
        for (int k = 0; k < 26; k++) if (cnt[k]) { ok = false; break; }
        if (ok) {
            for (int k = 1; k < len && !res; k++) {
                if (helper(s1, s2, i, j, k) && helper(s1, s2, i + k, j + k, len - k)) res = true;
                else if (helper(s1, s2, i, j + len - k, k) && helper(s1, s2, i + k, j, len - k)) res = true;
            }
        }
    }
    memo[i][j][len] = res ? 1 : 0;
    return res;
}

bool isScramble(char* s1, char* s2) {
    int n = strlen(s1);
    if ((int)strlen(s2) != n) return false;
    memset(memo, -1, sizeof(memo));
    return helper(s1, s2, 0, 0, n);
}
