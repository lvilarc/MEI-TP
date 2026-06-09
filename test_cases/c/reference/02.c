#include <string.h>
#include <stdbool.h>

bool isMatch(char* s, char* p) {
    int m = strlen(s), n = strlen(p);
    bool dp[30][30] = {{false}};
    dp[m][n] = true;
    for (int i = m; i >= 0; i--) {
        for (int j = n - 1; j >= 0; j--) {
            bool first = (i < m) && (p[j] == s[i] || p[j] == '.');
            if (j + 1 < n && p[j + 1] == '*') {
                dp[i][j] = dp[i][j + 2] || (first && dp[i + 1][j]);
            } else {
                dp[i][j] = first && dp[i + 1][j + 1];
            }
        }
    }
    return dp[0][0];
}
