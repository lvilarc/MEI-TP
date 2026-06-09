#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

int minCut(char* s) {
    int n = strlen(s);
    if (n <= 1) return 0;
    bool** pal = malloc(sizeof(bool*) * n);
    for (int i = 0; i < n; i++) pal[i] = calloc(n, sizeof(bool));
    int* dp = malloc(sizeof(int) * n);
    for (int i = 0; i < n; i++) {
        dp[i] = i; /* worst case: i cuts */
        for (int j = 0; j <= i; j++) {
            if (s[j] == s[i] && (i - j < 2 || pal[j + 1][i - 1])) {
                pal[j][i] = true;
                if (j == 0) dp[i] = 0;
                else if (dp[j - 1] + 1 < dp[i]) dp[i] = dp[j - 1] + 1;
            }
        }
    }
    int res = dp[n - 1];
    for (int i = 0; i < n; i++) free(pal[i]);
    free(pal);
    free(dp);
    return res;
}
