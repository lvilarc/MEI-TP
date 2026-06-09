#include <stdlib.h>
#include <string.h>

int numDistinct(char* s, char* t) {
    int m = strlen(s), n = strlen(t);
    unsigned long long* dp = calloc(n + 1, sizeof(unsigned long long));
    dp[0] = 1;
    for (int i = 0; i < m; i++) {
        for (int j = n; j >= 1; j--) {
            if (s[i] == t[j - 1]) dp[j] += dp[j - 1];
        }
    }
    int res = (int)dp[n];
    free(dp);
    return res;
}
